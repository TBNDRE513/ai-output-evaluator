from __future__ import annotations

import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable


@dataclass
class EvaluationResult:
    response_id: str
    correctness: int
    instruction_following: int
    clarity: int
    completeness: int
    safety: int
    total_score: int
    max_score: int = 25

    @property
    def percentage(self) -> float:
        return round((self.total_score / self.max_score) * 100, 1)


def clamp_score(value: int) -> int:
    """Keep rubric scores inside the allowed 1-5 range."""
    return max(1, min(5, int(value)))


def evaluate_response(response: dict) -> EvaluationResult:
    """
    Evaluate one AI response using five simple rubric categories.

    Expected score fields:
      - correctness
      - instruction_following
      - clarity
      - completeness
      - safety

    Each category is scored from 1 to 5.
    """
    response_id = str(response.get("id", "unknown"))

    scores = {
        "correctness": clamp_score(response.get("correctness", 1)),
        "instruction_following": clamp_score(response.get("instruction_following", 1)),
        "clarity": clamp_score(response.get("clarity", 1)),
        "completeness": clamp_score(response.get("completeness", 1)),
        "safety": clamp_score(response.get("safety", 1)),
    }

    total = sum(scores.values())

    return EvaluationResult(
        response_id=response_id,
        total_score=total,
        **scores,
    )


def load_responses(path: Path) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError("Input JSON must contain a list of response records.")
    return data


def evaluate_all(responses: Iterable[dict]) -> list[EvaluationResult]:
    return [evaluate_response(item) for item in responses]


def print_report(results: list[EvaluationResult]) -> None:
    print("AI OUTPUT EVALUATION REPORT")
    print("=" * 40)

    for result in results:
        print(
            f"{result.response_id}: "
            f"{result.total_score}/{result.max_score} "
            f"({result.percentage}%)"
        )

    if results:
        average = round(
            sum(r.percentage for r in results) / len(results), 1
        )
        print("-" * 40)
        print(f"Average score: {average}%")
    else:
        print("No responses found.")


def save_results(results: list[EvaluationResult], path: Path) -> None:
    payload = [
        {
            **asdict(result),
            "percentage": result.percentage,
        }
        for result in results
    ]
    path.write_text(
        json.dumps(payload, indent=2) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    project_dir = Path(__file__).resolve().parent
    input_path = project_dir / "sample_responses.json"
    output_path = project_dir / "evaluation_results.json"

    responses = load_responses(input_path)
    results = evaluate_all(responses)

    print_report(results)
    save_results(results, output_path)

    print(f"\nSaved detailed results to: {output_path.name}")


if __name__ == "__main__":
    main()
