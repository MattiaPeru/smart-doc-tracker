# Security Policy

Smart Doc Tracker processes potentially sensitive personal documents. Security
reports must be handled privately and must never include real document contents.

## Supported versions

Security fixes are currently applied to the latest commit on the default branch.
Formal long-term support begins when stable releases are published.

## Reporting a vulnerability

Do not open a public issue for a suspected vulnerability. Contact the repository
owner or the organization's private security channel. The project has no published
security address yet; deployments must replace this paragraph with the responsible
company contact before external distribution.

Include only the minimum information needed to reproduce the issue:

- affected version or commit;
- component and local configuration;
- sanitized reproduction steps;
- expected and observed behavior;
- potential impact.

Do not attach private documents, database dumps, OCR output, access tokens, host
usernames, absolute personal paths, or screenshots containing personal data.

## Security expectations

- MongoDB, ChromaDB, Ollama, and the FastAPI server must bind only to
  loopback by default.
- Local endpoints must reject credentials, remote hosts, HTTPS proxies, URL paths,
  query strings, and implicit ports unless a reviewed design explicitly changes the
  policy.
- Remote models, analytics, telemetry, automatic uploads, and remote storage are
  out of scope and prohibited.
- Sensitive content must not appear in logs, exception messages, notifications,
  test fixtures, or tracing systems.
- Web uploads must have size limits, allow-listed content types, generated temporary
  names, path traversal defenses, and deterministic cleanup.
- The web interface must implement CSRF protection where relevant, secure session
  handling if authentication is added, and restrictive browser security headers.
- Deletion must remove or explicitly retain every related representation according
  to documented policy: metadata, PDF sections, vector fragments, and managed files.

The application protects against accidental remote transmission by validating local
endpoints. It does not protect data from malware, privileged local users, compromised
dependencies, insecure host backups, or an already compromised operating system. See
[Privacy and security](docs/privacy-and-security.md) for the complete threat model.
