"""Shared test fixtures."""

from __future__ import annotations

import os
from pathlib import Path

import pytest

# Disable LangSmith tracing during tests
os.environ.setdefault("LANGCHAIN_TRACING_V2", "false")


@pytest.fixture()
def data_dir() -> Path:
    """Return the project data/ directory."""
    return Path(__file__).resolve().parent.parent / "data"


@pytest.fixture()
def pdf_path(data_dir: Path) -> Path:
    """Return the path to the HBR PDF."""
    return data_dir / "HBR_How_Apple_Is_Organized_For_Innovation.pdf"
