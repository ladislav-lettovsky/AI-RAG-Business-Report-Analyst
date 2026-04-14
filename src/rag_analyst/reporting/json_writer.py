"""Write structured JSON results to file."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from ..config import MODEL_EVALUATION, MODEL_GENERATION, RESULTS_DIR


def write_json_results(
    results: list[dict],
    output_dir: Path | None = None,
) -> Path:
    """Write run results as a timestamped JSON file.

    Parameters
    ----------
    results:
        List of dicts, each with keys: question, mode, response,
        and optionally evaluation.
    output_dir:
        Directory to write to. Defaults to RESULTS_DIR.

    Returns
    -------
    Path to the written JSON file.
    """
    output_dir = output_dir or RESULTS_DIR
    output_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    filepath = output_dir / f"run_{timestamp}.json"

    payload = {
        "run_timestamp": datetime.now(timezone.utc).isoformat(),
        "config": {
            "model_generation": MODEL_GENERATION,
            "model_evaluation": MODEL_EVALUATION,
        },
        "results": results,
    }

    filepath.write_text(json.dumps(payload, indent=2, default=str))
    return filepath
