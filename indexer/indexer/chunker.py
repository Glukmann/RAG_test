import re
from pathlib import Path
from typing import Any

import chardet

DOCS_EXTS = {".md", ".txt", ".rst", ".mdx"}
CODE_EXTS = {".mac"}
SUPPORTED_EXTS = DOCS_EXTS | CODE_EXTS


def read_text(path: Path) -> str:
    raw = path.read_bytes()
    try:
        return raw.decode("utf-8")
    except UnicodeDecodeError:
        detected = chardet.detect(raw)
        encoding = detected.get("encoding") or "utf-8"
        return raw.decode(encoding, errors="replace")


def chunk_document(path: Path) -> list[dict[str, Any]]:
    text = read_text(path)
    ext = path.suffix.lower()

    if ext == ".md":
        return chunk_markdown(text, path)
    if ext == ".mac":
        return chunk_mac_code(text, path)

    return chunk_plain(text, path)


def chunk_markdown(text: str, path: Path) -> list[dict[str, Any]]:
    lines = text.splitlines()
    chunks: list[dict[str, Any]] = []
    current: list[str] = []

    # Determine doc_type based on path / filename
    path_str = str(path).lower()
    fname = path.name.lower()
    if "practice" in path_str or "pattern_" in fname or "example" in fname:
        doc_type = "code_examples"
    else:
        doc_type = "docs"

    for line in lines:
        if line.startswith("#"):
            if current:
                chunks.append(_make_chunk("\n".join(current).strip(), path, doc_type, "markdown"))
            current = [line]
        else:
            current.append(line)

    if current:
        chunks.append(_make_chunk("\n".join(current).strip(), path, doc_type, "markdown"))

    # If no headers found, fall back to size-based chunking
    if len(chunks) == 1 and not lines[0].startswith("#") if lines else True:
        flat = "\n".join(lines)
        return split_by_size(flat, path, doc_type, "markdown", size=1200, overlap=200)

    return [c for c in chunks if c["text"]]


def chunk_plain(text: str, path: Path) -> list[dict[str, Any]]:
    return split_by_size(text, path, "docs", "text", size=1200, overlap=200)


def chunk_mac_code(text: str, path: Path) -> list[dict[str, Any]]:
    # Try to split on function definitions: name(...) := ...
    pattern = re.compile(
        r"(?ms)^\s*[a-zA-Z_][a-zA-Z0-9_]*\s*\([^)]*\)\s*:=.*?"
        r"(?=^\s*[a-zA-Z_][a-zA-Z0-9_]*\s*\([^)]*\)\s*:=|\Z)"
    )
    matches = list(pattern.finditer(text))

    chunks: list[dict[str, Any]] = []
    if matches:
        for m in matches:
            chunks.append(_make_chunk(m.group(0).strip(), path, "code_examples", "mac"))
    else:
        # Fallback: split by blank lines preserving boundaries
        blocks = re.split(r"\n\s*\n", text.strip())
        for block in blocks:
            if len(block) > 1500:
                chunks.extend(
                    split_by_size(block, path, "code_examples", "mac", size=1500, overlap=100)
                )
            else:
                chunks.append(_make_chunk(block.strip(), path, "code_examples", "mac"))

    return [c for c in chunks if c["text"]]


def split_by_size(
    text: str,
    path: Path,
    doc_type: str,
    language: str,
    size: int,
    overlap: int,
) -> list[dict[str, Any]]:
    chunks: list[dict[str, Any]] = []
    start = 0
    text_len = len(text)
    while start < text_len:
        end = min(start + size, text_len)
        chunks.append(_make_chunk(text[start:end].strip(), path, doc_type, language))
        if end == text_len:
            break
        start = end - overlap
    return chunks


def _make_chunk(text: str, path: Path, doc_type: str, language: str) -> dict[str, Any]:
    return {
        "text": text,
        "source": str(path),
        "doc_type": doc_type,
        "language": language,
        "file_ext": path.suffix,
    }
