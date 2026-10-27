# AI Output Evaluator

A small Python portfolio project that demonstrates a simple, transparent rubric for evaluating AI-generated responses.

## What this project demonstrates

- Python
- JSON parsing
- Structured scoring
- Dataclasses
- File input/output
- Basic automated testing
- AI response evaluation
- Clear and explainable decision logic

## Evaluation rubric

Each response receives a score from **1 to 5** in five categories:

1. Correctness
2. Instruction following
3. Clarity
4. Completeness
5. Safety

The evaluator calculates a total score out of 25 and converts it to a percentage.

## Run the project

```bash
python evaluator.py
```

The program reads `sample_responses.json`, prints a summary report, and writes detailed results to `evaluation_results.json`.

## Run the tests

```bash
python -m unittest test_evaluator.py
```

## Example output

```text
AI OUTPUT EVALUATION REPORT
========================================
response_001: 24/25 (96.0%)
response_002: 25/25 (100.0%)
response_003: 24/25 (96.0%)
----------------------------------------
Average score: 97.3%
```

## Why I built this

I created this project as a practical demonstration of Python-based AI response evaluation. The goal is to show how subjective quality criteria can be converted into a simple, structured, and auditable scoring workflow.

## Author

Stephen Burks
