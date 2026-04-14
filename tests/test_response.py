"""Tests for response modes — needs API key."""

from __future__ import annotations

import os

import pytest

HAS_API_KEY = bool(os.environ.get("OPENAI_API_KEY"))
pytestmark = pytest.mark.skipif(not HAS_API_KEY, reason="OPENAI_API_KEY not set")


class TestResponses:
    @pytest.fixture(autouse=True)
    def _setup(self):
        from rag_analyst.ingest import build_vectorstore, chunk_documents

        self.document_chunks = chunk_documents()
        self.vectorstore = build_vectorstore(self.document_chunks)

    def test_llm_response_returns_string(self):
        from rag_analyst.response import llm_response

        result = llm_response("What is Apple?")
        assert isinstance(result, str)
        assert len(result) > 0

    def test_eng_response_returns_string(self):
        from rag_analyst.response import eng_response

        result = eng_response("What is Apple?")
        assert isinstance(result, str)
        assert len(result) > 0

    def test_rag_response_returns_string(self):
        from rag_analyst.response import rag_response

        result = rag_response(
            "Who are the authors?",
            self.vectorstore,
            self.document_chunks,
        )
        assert isinstance(result, str)
        assert len(result) > 0
