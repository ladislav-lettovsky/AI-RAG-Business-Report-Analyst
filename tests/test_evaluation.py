"""Tests for evaluation — needs API key."""

from __future__ import annotations

import os

import pytest

HAS_API_KEY = bool(os.environ.get("OPENAI_API_KEY"))
pytestmark = pytest.mark.skipif(not HAS_API_KEY, reason="OPENAI_API_KEY not set")


class TestEvaluation:
    def test_evaluation_returns_scores(self):
        from rag_analyst.evaluation import response_evaluation

        result = response_evaluation(
            content="Apple is organized for innovation with functional expertise.",
            question="How is Apple organized?",
            response="Apple uses a functional organization to drive innovation.",
        )
        assert isinstance(result, str)
        assert "groundedness" in result.lower() or "precision" in result.lower()
