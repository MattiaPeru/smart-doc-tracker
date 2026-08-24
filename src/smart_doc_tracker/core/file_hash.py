"""Deterministic hashing for local document files."""

from __future__ import annotations

from hashlib import sha256
from pathlib import Path


class FileHashingError(RuntimeError):
    """Raised when a local document cannot be hashed safely."""


def calculate_file_sha256(file_path: str | Path, *, chunk_size: int = 1024 * 1024) -> str:
    """Return the lowercase SHA-256 digest of a local file."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")

    path = Path(file_path).expanduser()
    if not path.exists():
        raise FileHashingError("The document file does not exist.")
    if not path.is_file():
        raise FileHashingError("The document path must refer to a file.")

    digest = sha256()
    try:
        with path.open("rb") as document_file:
            while chunk := document_file.read(chunk_size):
                digest.update(chunk)
    except OSError as exc:
        raise FileHashingError("The document file could not be hashed.") from exc
    return digest.hexdigest()
