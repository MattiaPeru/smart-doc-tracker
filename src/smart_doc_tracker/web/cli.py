"""Command-line startup for the loopback-only dashboard."""

import argparse
import logging
import os
from collections.abc import Callable, Sequence

from .local_services import LocalServiceStartupError, LocalWebServiceManager

_LOG_LEVELS = ("debug", "info", "warning", "error", "critical")


def run(
    argv: Sequence[str] | None = None,
    *,
    service_manager_factory: Callable[[], LocalWebServiceManager] = (
        LocalWebServiceManager
    ),
) -> None:
    """Run the dashboard and own its required local service lifecycle."""
    parser = argparse.ArgumentParser(description="Run the local document dashboard.")
    parser.add_argument("--host", default="127.0.0.1", choices=("127.0.0.1", "::1"))
    parser.add_argument("--port", type=int, default=8080)
    parser.add_argument(
        "--log-level",
        choices=_LOG_LEVELS,
        default="info",
        help="Terminal detail level (default: info).",
    )
    parser.add_argument(
        "--access-log",
        action="store_true",
        help="Show one terminal line for every HTTP request.",
    )
    parser.add_argument(
        "--chat-debug",
        action="store_true",
        help=(
            "Show chat retrieval, document excerpts, prompts, model output, "
            "and errors in the terminal."
        ),
    )
    arguments = parser.parse_args(argv)
    if not 1 <= arguments.port <= 65_535:
        parser.error("--port must be between 1 and 65535")
    _configure_application_logging(
        "info" if arguments.chat_debug else arguments.log_level
    )
    import uvicorn

    services = service_manager_factory()
    previous_chat_debug = os.environ.get("SMART_DOC_TRACKER_CHAT_DEBUG")
    try:
        if arguments.chat_debug:
            os.environ["SMART_DOC_TRACKER_CHAT_DEBUG"] = "1"
        services.start()
        uvicorn.run(
            "smart_doc_tracker.web.app:create_app",
            factory=True,
            host=arguments.host,
            port=arguments.port,
            workers=1,
            log_level=arguments.log_level,
            access_log=arguments.access_log,
        )
    except LocalServiceStartupError as exc:
        parser.exit(status=1, message=f"error: {exc}\n")
    finally:
        services.stop()
        if arguments.chat_debug:
            if previous_chat_debug is None:
                os.environ.pop("SMART_DOC_TRACKER_CHAT_DEBUG", None)
            else:
                os.environ["SMART_DOC_TRACKER_CHAT_DEBUG"] = previous_chat_debug


def _configure_application_logging(level: str) -> None:
    """Send application progress and safe diagnostics to the server terminal."""
    application_logger = logging.getLogger("smart_doc_tracker")
    handler = logging.StreamHandler()
    handler.setFormatter(
        logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
            datefmt="%H:%M:%S",
        )
    )
    application_logger.handlers.clear()
    application_logger.addHandler(handler)
    application_logger.setLevel(level.upper())
    application_logger.propagate = False
