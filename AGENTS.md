# Smart Doc Tracker Guidance

## Repository navigation

- Read `docs/agent/README.md` before exploring the source tree.
- Use `docs/agent/ARCHITECTURE.md` and `docs/agent/WORKFLOWS.md` to identify the
  responsible component and its dependencies.
- Search `docs/agent/PUBLIC_API.md` for public signatures before opening source.
- Inspect implementation files and focused tests only when required by the task.
- Regenerate the public API reference after changing public classes, functions,
  methods, models, or protocols with
  `.venv\Scripts\python.exe scripts\generate_agent_reference.py`.

## Language

- Write all generated code strictly in English.
- Write identifiers, comments, docstrings, exceptions, log messages, and strings embedded in code strictly in English.

## Architecture

- Target Python 3.11 or newer.
- Keep OCR, parsing, persistence, notifications, and pipeline orchestration in separate modules or packages.
- Keep `ocr` responsible only for reading local files and extracting raw text.
- Keep `parser` responsible only for converting raw text into validated domain models.
- Keep `db` responsible only for local persistence and queries.
- Keep `notifier` responsible only for local desktop notifications and accept prepared notification data.
- Keep cross-component coordination in `pipeline` and depend on narrow public interfaces.
- Prefer small, typed, testable components and explicit dependency injection over shared global state.

## Privacy

- Preserve a fully offline, privacy-first architecture.
- Do not add outbound network calls, cloud services, remote APIs, telemetry, analytics, hosted models, or remote storage.
- Allow local-only services such as Ollama only when bound to loopback and configured never to transmit data outside the host.
- Avoid logging document contents, raw OCR text, credentials, or sensitive personal fields.
- Remove temporary files deterministically, including after exceptions.
- Validate and normalize extracted data before persistence.

## Implementation and Verification

- Provide a clean, working implementation directly without enumerating defects in previous code.
- Mention genuine blockers or failed verification when the user needs that information.
- Add or update focused tests for changed behavior.
- Keep tests offline and deterministic.
- Preserve existing repository conventions unless they conflict with this guidance.
