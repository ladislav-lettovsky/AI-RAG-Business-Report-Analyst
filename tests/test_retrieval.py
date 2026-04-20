"""Tests for retrieval — needs API key for embeddings."""

from __future__ import annotations

import os

import pytest

HAS_API_KEY = bool(os.environ.get("OPENAI_API_KEY"))
pytestmark = pytest.mark.skipif(not HAS_API_KEY, reason="OPENAI_API_KEY not set")


class TestRetrieval:
    @pytest.fixture(autouse=True)
    def _setup(self):
        from rag_analyst.ingest import build_vectorstore, chunk_documents

        self.document_chunks = chunk_documents()
        self.vectorstore = build_vectorstore(self.document_chunks)

    def test_build_vectorstore(self):
        assert self.vectorstore is not None

    def test_retrieve_context_returns_string(self):
        from rag_analyst.retrieval import retrieve_context

        context = retrieve_context("Who are the authors?", self.vectorstore, self.document_chunks)
        assert isinstance(context, str)
        assert len(context) > 0

    def test_first_chunk_injection(self):
        from rag_analyst.retrieval import retrieve_context

        first_chunk_content = self.document_chunks[0].page_content
        context = retrieve_context("What is innovation?", self.vectorstore, self.document_chunks)
        assert first_chunk_content in context
