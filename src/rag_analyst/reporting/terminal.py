"""Terminal comparison table printer."""

from __future__ import annotations


def print_comparison(results: list[dict]) -> None:
    """Print a formatted comparison table of responses across modes.

    Parameters
    ----------
    results:
        List of dicts with keys: question, mode, response,
        and optionally evaluation.
    """
    # Group results by question
    questions: dict[str, list[dict]] = {}
    for r in results:
        questions.setdefault(r["question"], []).append(r)

    separator = "=" * 80

    for question, entries in questions.items():
        print(f"\n{separator}")
        print(f"  Q: {question}")
        print(separator)

        for entry in entries:
            mode = entry["mode"].upper()
            response = entry["response"]
            evaluation = entry.get("evaluation", "")

            print(f"\n  [{mode}]")
            print(f"  {response[:500]}{'...' if len(response) > 500 else ''}")

            if evaluation:
                print(f"  Evaluation: {evaluation}")

        print()
