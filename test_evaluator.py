import unittest

from evaluator import clamp_score, evaluate_response


class EvaluatorTests(unittest.TestCase):
    def test_clamp_score_limits_values(self):
        self.assertEqual(clamp_score(0), 1)
        self.assertEqual(clamp_score(3), 3)
        self.assertEqual(clamp_score(8), 5)

    def test_evaluate_response_total(self):
        response = {
            "id": "test_001",
            "correctness": 5,
            "instruction_following": 4,
            "clarity": 3,
            "completeness": 2,
            "safety": 5,
        }

        result = evaluate_response(response)

        self.assertEqual(result.response_id, "test_001")
        self.assertEqual(result.total_score, 19)
        self.assertEqual(result.percentage, 76.0)


if __name__ == "__main__":
    unittest.main()
