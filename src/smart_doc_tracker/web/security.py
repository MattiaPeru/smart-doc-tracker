"""Enforce loopback-only browser access and restrictive response policies."""

import logging
import secrets
from collections.abc import Awaitable, Callable
from urllib.parse import urlsplit

from fastapi import Request
from fastapi.staticfiles import StaticFiles
from starlette.responses import Response
from starlette.types import Scope

_LOGGER = logging.getLogger("smart_doc_tracker.web.app")
_LOOPBACK_HOSTS = frozenset({"127.0.0.1", "localhost", "::1"})
_UNSAFE_METHODS = frozenset({"POST", "PUT", "PATCH", "DELETE"})
_CSRF_HEADER = "X-Smart-Doc-CSRF"
_CONTENT_SECURITY_POLICY = "; ".join(
    (
        "default-src 'self'",
        "base-uri 'none'",
        "connect-src 'self'",
        "form-action 'self'",
        "frame-ancestors 'none'",
        "img-src 'self' data:",
        "object-src 'none'",
        "script-src 'self'",
        "style-src 'self'",
    )
)


class LocalStaticFiles(StaticFiles):
    """Serve local dashboard assets without retaining stale browser copies."""

    async def get_response(self, path: str, scope: Scope) -> Response:
        """Return one static asset with browser persistence disabled."""
        response = await super().get_response(path, scope)
        response.headers["Cache-Control"] = "no-store, max-age=0"
        return response


class LocalWebSecurity:
    """Protect local routes from external hosts, cross-origin writes, and CSRF."""

    def __init__(self, csrf_token: str) -> None:
        """Require the given token on browser mutation requests."""
        self._csrf_token = csrf_token

    async def enforce(
        self,
        request: Request,
        call_next: Callable[[Request], Awaitable[Response]],
    ) -> Response:
        """Validate request authority and apply browser policies to responses."""
        host = request.headers.get("host", "")
        if self._normalized_authority(host) is None:
            return self._secure_response(Response(status_code=400))
        origin = request.headers.get("origin")
        if origin is not None and not self._same_loopback_origin(origin, host):
            return self._secure_response(Response(status_code=403))
        if request.method in _UNSAFE_METHODS:
            supplied_token = request.headers.get(_CSRF_HEADER, "")
            if not secrets.compare_digest(supplied_token, self._csrf_token):
                return self._secure_response(Response(status_code=403))
        try:
            response = await call_next(request)
        except Exception as exc:
            _LOGGER.error(
                "Request %s failed with an unhandled %s.",
                request.method,
                type(exc).__name__,
            )
            raise
        if response.status_code >= 500:
            route = request.scope.get("route")
            route_pattern = getattr(route, "path", "unmatched route")
            _LOGGER.error(
                "Request %s %s returned HTTP %s.",
                request.method,
                route_pattern,
                response.status_code,
            )
        return self._secure_response(response)

    @staticmethod
    def _normalized_authority(value: str) -> tuple[str, int] | None:
        """Parse an HTTP authority and accept only an exact loopback hostname."""
        if not value or any(character in value for character in "/?#@"):
            return None
        try:
            parsed = urlsplit(f"//{value}")
            port = parsed.port or 80
        except ValueError:
            return None
        hostname = parsed.hostname.lower() if parsed.hostname is not None else None
        if hostname not in _LOOPBACK_HOSTS:
            return None
        return hostname, port

    def _same_loopback_origin(self, origin: str, host: str) -> bool:
        """Require browser requests to originate from the served authority."""
        try:
            parsed = urlsplit(origin)
            origin_authority = self._normalized_authority(parsed.netloc)
        except ValueError:
            return False
        return (
            parsed.scheme == "http"
            and parsed.path == ""
            and parsed.query == ""
            and parsed.fragment == ""
            and origin_authority is not None
            and origin_authority == self._normalized_authority(host)
        )

    @staticmethod
    def _secure_response(response: Response) -> Response:
        """Apply restrictive browser policies to every local HTTP response."""
        response.headers["Content-Security-Policy"] = _CONTENT_SECURITY_POLICY
        response.headers["Cross-Origin-Opener-Policy"] = "same-origin"
        response.headers["Cross-Origin-Resource-Policy"] = "same-origin"
        response.headers["Permissions-Policy"] = (
            "camera=(), geolocation=(), microphone=(), payment=(), usb=()"
        )
        response.headers["Referrer-Policy"] = "no-referrer"
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        return response
