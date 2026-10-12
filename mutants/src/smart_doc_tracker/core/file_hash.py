"""Deterministic hashing for local document files."""

from __future__ import annotations

from hashlib import sha256
from pathlib import Path


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class FileHashingError(RuntimeError):
    """Raised when a local document cannot be hashed safely."""
mutants_x_calculate_file_sha256__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_calculate_file_sha256__mutmut)
def calculate_file_sha256(
    file_path: str | Path, *, chunk_size: int = 1024 * 1024
) -> str:
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


def x_calculate_file_sha256__mutmut_orig(
    file_path: str | Path, *, chunk_size: int = 1024 * 1024
) -> str:
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


def x_calculate_file_sha256__mutmut_1(
    file_path: str | Path, *, chunk_size: int = 1024 * 1024
) -> str:
    """Return the lowercase SHA-256 digest of a local file."""
    if chunk_size < 0:
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


def x_calculate_file_sha256__mutmut_2(
    file_path: str | Path, *, chunk_size: int = 1024 * 1024
) -> str:
    """Return the lowercase SHA-256 digest of a local file."""
    if chunk_size <= 1:
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


def x_calculate_file_sha256__mutmut_3(
    file_path: str | Path, *, chunk_size: int = 1024 * 1024
) -> str:
    """Return the lowercase SHA-256 digest of a local file."""
    if chunk_size <= 0:
        raise ValueError(None)

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


def x_calculate_file_sha256__mutmut_4(
    file_path: str | Path, *, chunk_size: int = 1024 * 1024
) -> str:
    """Return the lowercase SHA-256 digest of a local file."""
    if chunk_size <= 0:
        raise ValueError("XXchunk_size must be positiveXX")

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


def x_calculate_file_sha256__mutmut_5(
    file_path: str | Path, *, chunk_size: int = 1024 * 1024
) -> str:
    """Return the lowercase SHA-256 digest of a local file."""
    if chunk_size <= 0:
        raise ValueError("CHUNK_SIZE MUST BE POSITIVE")

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


def x_calculate_file_sha256__mutmut_6(
    file_path: str | Path, *, chunk_size: int = 1024 * 1024
) -> str:
    """Return the lowercase SHA-256 digest of a local file."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")

    path = None
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


def x_calculate_file_sha256__mutmut_7(
    file_path: str | Path, *, chunk_size: int = 1024 * 1024
) -> str:
    """Return the lowercase SHA-256 digest of a local file."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")

    path = Path(None).expanduser()
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


def x_calculate_file_sha256__mutmut_8(
    file_path: str | Path, *, chunk_size: int = 1024 * 1024
) -> str:
    """Return the lowercase SHA-256 digest of a local file."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")

    path = Path(file_path).expanduser()
    if path.exists():
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


def x_calculate_file_sha256__mutmut_9(
    file_path: str | Path, *, chunk_size: int = 1024 * 1024
) -> str:
    """Return the lowercase SHA-256 digest of a local file."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")

    path = Path(file_path).expanduser()
    if not path.exists():
        raise FileHashingError(None)
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


def x_calculate_file_sha256__mutmut_10(
    file_path: str | Path, *, chunk_size: int = 1024 * 1024
) -> str:
    """Return the lowercase SHA-256 digest of a local file."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")

    path = Path(file_path).expanduser()
    if not path.exists():
        raise FileHashingError("XXThe document file does not exist.XX")
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


def x_calculate_file_sha256__mutmut_11(
    file_path: str | Path, *, chunk_size: int = 1024 * 1024
) -> str:
    """Return the lowercase SHA-256 digest of a local file."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")

    path = Path(file_path).expanduser()
    if not path.exists():
        raise FileHashingError("the document file does not exist.")
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


def x_calculate_file_sha256__mutmut_12(
    file_path: str | Path, *, chunk_size: int = 1024 * 1024
) -> str:
    """Return the lowercase SHA-256 digest of a local file."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")

    path = Path(file_path).expanduser()
    if not path.exists():
        raise FileHashingError("THE DOCUMENT FILE DOES NOT EXIST.")
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


def x_calculate_file_sha256__mutmut_13(
    file_path: str | Path, *, chunk_size: int = 1024 * 1024
) -> str:
    """Return the lowercase SHA-256 digest of a local file."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")

    path = Path(file_path).expanduser()
    if not path.exists():
        raise FileHashingError("The document file does not exist.")
    if path.is_file():
        raise FileHashingError("The document path must refer to a file.")

    digest = sha256()
    try:
        with path.open("rb") as document_file:
            while chunk := document_file.read(chunk_size):
                digest.update(chunk)
    except OSError as exc:
        raise FileHashingError("The document file could not be hashed.") from exc
    return digest.hexdigest()


def x_calculate_file_sha256__mutmut_14(
    file_path: str | Path, *, chunk_size: int = 1024 * 1024
) -> str:
    """Return the lowercase SHA-256 digest of a local file."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")

    path = Path(file_path).expanduser()
    if not path.exists():
        raise FileHashingError("The document file does not exist.")
    if not path.is_file():
        raise FileHashingError(None)

    digest = sha256()
    try:
        with path.open("rb") as document_file:
            while chunk := document_file.read(chunk_size):
                digest.update(chunk)
    except OSError as exc:
        raise FileHashingError("The document file could not be hashed.") from exc
    return digest.hexdigest()


def x_calculate_file_sha256__mutmut_15(
    file_path: str | Path, *, chunk_size: int = 1024 * 1024
) -> str:
    """Return the lowercase SHA-256 digest of a local file."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")

    path = Path(file_path).expanduser()
    if not path.exists():
        raise FileHashingError("The document file does not exist.")
    if not path.is_file():
        raise FileHashingError("XXThe document path must refer to a file.XX")

    digest = sha256()
    try:
        with path.open("rb") as document_file:
            while chunk := document_file.read(chunk_size):
                digest.update(chunk)
    except OSError as exc:
        raise FileHashingError("The document file could not be hashed.") from exc
    return digest.hexdigest()


def x_calculate_file_sha256__mutmut_16(
    file_path: str | Path, *, chunk_size: int = 1024 * 1024
) -> str:
    """Return the lowercase SHA-256 digest of a local file."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")

    path = Path(file_path).expanduser()
    if not path.exists():
        raise FileHashingError("The document file does not exist.")
    if not path.is_file():
        raise FileHashingError("the document path must refer to a file.")

    digest = sha256()
    try:
        with path.open("rb") as document_file:
            while chunk := document_file.read(chunk_size):
                digest.update(chunk)
    except OSError as exc:
        raise FileHashingError("The document file could not be hashed.") from exc
    return digest.hexdigest()


def x_calculate_file_sha256__mutmut_17(
    file_path: str | Path, *, chunk_size: int = 1024 * 1024
) -> str:
    """Return the lowercase SHA-256 digest of a local file."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")

    path = Path(file_path).expanduser()
    if not path.exists():
        raise FileHashingError("The document file does not exist.")
    if not path.is_file():
        raise FileHashingError("THE DOCUMENT PATH MUST REFER TO A FILE.")

    digest = sha256()
    try:
        with path.open("rb") as document_file:
            while chunk := document_file.read(chunk_size):
                digest.update(chunk)
    except OSError as exc:
        raise FileHashingError("The document file could not be hashed.") from exc
    return digest.hexdigest()


def x_calculate_file_sha256__mutmut_18(
    file_path: str | Path, *, chunk_size: int = 1024 * 1024
) -> str:
    """Return the lowercase SHA-256 digest of a local file."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")

    path = Path(file_path).expanduser()
    if not path.exists():
        raise FileHashingError("The document file does not exist.")
    if not path.is_file():
        raise FileHashingError("The document path must refer to a file.")

    digest = None
    try:
        with path.open("rb") as document_file:
            while chunk := document_file.read(chunk_size):
                digest.update(chunk)
    except OSError as exc:
        raise FileHashingError("The document file could not be hashed.") from exc
    return digest.hexdigest()


def x_calculate_file_sha256__mutmut_19(
    file_path: str | Path, *, chunk_size: int = 1024 * 1024
) -> str:
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
        with path.open(None) as document_file:
            while chunk := document_file.read(chunk_size):
                digest.update(chunk)
    except OSError as exc:
        raise FileHashingError("The document file could not be hashed.") from exc
    return digest.hexdigest()


def x_calculate_file_sha256__mutmut_20(
    file_path: str | Path, *, chunk_size: int = 1024 * 1024
) -> str:
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
        with path.open("XXrbXX") as document_file:
            while chunk := document_file.read(chunk_size):
                digest.update(chunk)
    except OSError as exc:
        raise FileHashingError("The document file could not be hashed.") from exc
    return digest.hexdigest()


def x_calculate_file_sha256__mutmut_21(
    file_path: str | Path, *, chunk_size: int = 1024 * 1024
) -> str:
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
        with path.open("RB") as document_file:
            while chunk := document_file.read(chunk_size):
                digest.update(chunk)
    except OSError as exc:
        raise FileHashingError("The document file could not be hashed.") from exc
    return digest.hexdigest()


def x_calculate_file_sha256__mutmut_22(
    file_path: str | Path, *, chunk_size: int = 1024 * 1024
) -> str:
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
            while chunk := document_file.read(None):
                digest.update(chunk)
    except OSError as exc:
        raise FileHashingError("The document file could not be hashed.") from exc
    return digest.hexdigest()


def x_calculate_file_sha256__mutmut_23(
    file_path: str | Path, *, chunk_size: int = 1024 * 1024
) -> str:
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
                digest.update(None)
    except OSError as exc:
        raise FileHashingError("The document file could not be hashed.") from exc
    return digest.hexdigest()


def x_calculate_file_sha256__mutmut_24(
    file_path: str | Path, *, chunk_size: int = 1024 * 1024
) -> str:
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
        raise FileHashingError(None) from exc
    return digest.hexdigest()


def x_calculate_file_sha256__mutmut_25(
    file_path: str | Path, *, chunk_size: int = 1024 * 1024
) -> str:
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
        raise FileHashingError("XXThe document file could not be hashed.XX") from exc
    return digest.hexdigest()


def x_calculate_file_sha256__mutmut_26(
    file_path: str | Path, *, chunk_size: int = 1024 * 1024
) -> str:
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
        raise FileHashingError("the document file could not be hashed.") from exc
    return digest.hexdigest()


def x_calculate_file_sha256__mutmut_27(
    file_path: str | Path, *, chunk_size: int = 1024 * 1024
) -> str:
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
        raise FileHashingError("THE DOCUMENT FILE COULD NOT BE HASHED.") from exc
    return digest.hexdigest()

mutants_x_calculate_file_sha256__mutmut['_mutmut_orig'] = x_calculate_file_sha256__mutmut_orig # type: ignore # mutmut generated
mutants_x_calculate_file_sha256__mutmut['x_calculate_file_sha256__mutmut_1'] = x_calculate_file_sha256__mutmut_1 # type: ignore # mutmut generated
mutants_x_calculate_file_sha256__mutmut['x_calculate_file_sha256__mutmut_2'] = x_calculate_file_sha256__mutmut_2 # type: ignore # mutmut generated
mutants_x_calculate_file_sha256__mutmut['x_calculate_file_sha256__mutmut_3'] = x_calculate_file_sha256__mutmut_3 # type: ignore # mutmut generated
mutants_x_calculate_file_sha256__mutmut['x_calculate_file_sha256__mutmut_4'] = x_calculate_file_sha256__mutmut_4 # type: ignore # mutmut generated
mutants_x_calculate_file_sha256__mutmut['x_calculate_file_sha256__mutmut_5'] = x_calculate_file_sha256__mutmut_5 # type: ignore # mutmut generated
mutants_x_calculate_file_sha256__mutmut['x_calculate_file_sha256__mutmut_6'] = x_calculate_file_sha256__mutmut_6 # type: ignore # mutmut generated
mutants_x_calculate_file_sha256__mutmut['x_calculate_file_sha256__mutmut_7'] = x_calculate_file_sha256__mutmut_7 # type: ignore # mutmut generated
mutants_x_calculate_file_sha256__mutmut['x_calculate_file_sha256__mutmut_8'] = x_calculate_file_sha256__mutmut_8 # type: ignore # mutmut generated
mutants_x_calculate_file_sha256__mutmut['x_calculate_file_sha256__mutmut_9'] = x_calculate_file_sha256__mutmut_9 # type: ignore # mutmut generated
mutants_x_calculate_file_sha256__mutmut['x_calculate_file_sha256__mutmut_10'] = x_calculate_file_sha256__mutmut_10 # type: ignore # mutmut generated
mutants_x_calculate_file_sha256__mutmut['x_calculate_file_sha256__mutmut_11'] = x_calculate_file_sha256__mutmut_11 # type: ignore # mutmut generated
mutants_x_calculate_file_sha256__mutmut['x_calculate_file_sha256__mutmut_12'] = x_calculate_file_sha256__mutmut_12 # type: ignore # mutmut generated
mutants_x_calculate_file_sha256__mutmut['x_calculate_file_sha256__mutmut_13'] = x_calculate_file_sha256__mutmut_13 # type: ignore # mutmut generated
mutants_x_calculate_file_sha256__mutmut['x_calculate_file_sha256__mutmut_14'] = x_calculate_file_sha256__mutmut_14 # type: ignore # mutmut generated
mutants_x_calculate_file_sha256__mutmut['x_calculate_file_sha256__mutmut_15'] = x_calculate_file_sha256__mutmut_15 # type: ignore # mutmut generated
mutants_x_calculate_file_sha256__mutmut['x_calculate_file_sha256__mutmut_16'] = x_calculate_file_sha256__mutmut_16 # type: ignore # mutmut generated
mutants_x_calculate_file_sha256__mutmut['x_calculate_file_sha256__mutmut_17'] = x_calculate_file_sha256__mutmut_17 # type: ignore # mutmut generated
mutants_x_calculate_file_sha256__mutmut['x_calculate_file_sha256__mutmut_18'] = x_calculate_file_sha256__mutmut_18 # type: ignore # mutmut generated
mutants_x_calculate_file_sha256__mutmut['x_calculate_file_sha256__mutmut_19'] = x_calculate_file_sha256__mutmut_19 # type: ignore # mutmut generated
mutants_x_calculate_file_sha256__mutmut['x_calculate_file_sha256__mutmut_20'] = x_calculate_file_sha256__mutmut_20 # type: ignore # mutmut generated
mutants_x_calculate_file_sha256__mutmut['x_calculate_file_sha256__mutmut_21'] = x_calculate_file_sha256__mutmut_21 # type: ignore # mutmut generated
mutants_x_calculate_file_sha256__mutmut['x_calculate_file_sha256__mutmut_22'] = x_calculate_file_sha256__mutmut_22 # type: ignore # mutmut generated
mutants_x_calculate_file_sha256__mutmut['x_calculate_file_sha256__mutmut_23'] = x_calculate_file_sha256__mutmut_23 # type: ignore # mutmut generated
mutants_x_calculate_file_sha256__mutmut['x_calculate_file_sha256__mutmut_24'] = x_calculate_file_sha256__mutmut_24 # type: ignore # mutmut generated
mutants_x_calculate_file_sha256__mutmut['x_calculate_file_sha256__mutmut_25'] = x_calculate_file_sha256__mutmut_25 # type: ignore # mutmut generated
mutants_x_calculate_file_sha256__mutmut['x_calculate_file_sha256__mutmut_26'] = x_calculate_file_sha256__mutmut_26 # type: ignore # mutmut generated
mutants_x_calculate_file_sha256__mutmut['x_calculate_file_sha256__mutmut_27'] = x_calculate_file_sha256__mutmut_27 # type: ignore # mutmut generated
