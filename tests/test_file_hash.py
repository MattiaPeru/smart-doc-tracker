from __future__ import annotations

from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase

from core.file_hash import FileHashingError, calculate_file_sha256


class FileHashTests(TestCase):
    def test_calculates_sha256_in_chunks(self) -> None:
        with TemporaryDirectory() as directory:
            path = Path(directory) / "document.bin"
            path.write_bytes(b"private local document")

            digest = calculate_file_sha256(path, chunk_size=3)

        self.assertEqual(
            digest,
            "bd6f355dbfcd199988c0cf24c627493b8e7b244b3194c565993343f2e101b303",
        )

    def test_rejects_missing_file_without_exposing_path(self) -> None:
        with TemporaryDirectory() as directory:
            path = Path(directory) / "sensitive-name.pdf"

            with self.assertRaises(FileHashingError) as raised:
                calculate_file_sha256(path)

        self.assertNotIn("sensitive-name", str(raised.exception))

    def test_rejects_invalid_chunk_size(self) -> None:
        with self.assertRaisesRegex(ValueError, "positive"):
            calculate_file_sha256("unused", chunk_size=0)
