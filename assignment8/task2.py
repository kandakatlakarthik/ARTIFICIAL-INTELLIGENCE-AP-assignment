import unittest

def assign_grade(score: int | float) -> str:
    """
    Assigns a letter grade based on a numerical score.

    Grading scale:
    - 90-100: 'A'
    - 80-89:  'B'
    - 70-79:  'C'
    - 60-69:  'D'
    - 0-59:   'F'

    Args:
        score: A numerical score between 0 and 100.

    Returns:
        The corresponding letter grade as a string.

    Raises:
        TypeError: If the score is not a number (int or float).
        ValueError: If the score is outside the valid range of 0-100.
    """
    if not isinstance(score, (int, float)):
        raise TypeError("Score must be a numeric value.")
    if not 0 <= score <= 100:
        raise ValueError("Score must be between 0 and 100, inclusive.")

    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

class TestAssignGrade(unittest.TestCase):
    """Test suite for the assign_grade function."""

    def test_grade_a(self):
        """Test scores that should result in grade 'A'."""
        self.assertEqual(assign_grade(95), 'A')
        self.assertEqual(assign_grade(100), 'A')
        self.assertEqual(assign_grade(90), 'A')

    def test_grade_b(self):
        """Test scores that should result in grade 'B'."""
        self.assertEqual(assign_grade(85), 'B')
        self.assertEqual(assign_grade(89.9), 'B')
        self.assertEqual(assign_grade(80), 'B')

    def test_grade_c(self):
        """Test scores that should result in grade 'C'."""
        self.assertEqual(assign_grade(75), 'C')
        self.assertEqual(assign_grade(79), 'C')
        self.assertEqual(assign_grade(70), 'C')

    def test_grade_d(self):
        """Test scores that should result in grade 'D'."""
        self.assertEqual(assign_grade(65), 'D')
        self.assertEqual(assign_grade(69), 'D')
        self.assertEqual(assign_grade(60), 'D')

    def test_grade_f(self):
        """Test scores that should result in grade 'F'."""
        self.assertEqual(assign_grade(59), 'F')
        self.assertEqual(assign_grade(30), 'F')
        self.assertEqual(assign_grade(0), 'F')

    def test_boundary_values(self):
        """Test the exact boundary values for each grade."""
        test_cases = {
            100: 'A',
            90: 'A',
            89.99: 'B',
            80: 'B',
            79.99: 'C',
            70: 'C',
            69.99: 'D',
            60: 'D',
            59.99: 'F',
            0: 'F'
        }
        for score, expected_grade in test_cases.items():
            with self.subTest(score=score):
                self.assertEqual(assign_grade(score), expected_grade)

    def test_invalid_score_range(self):
        """Test scores outside the valid range [0, 100]."""
        invalid_scores = [-10, -5, -0.1, 100.1, 105]
        for score in invalid_scores:
            with self.subTest(score=score):
                with self.assertRaises(ValueError):
                    assign_grade(score)

    def test_invalid_input_types(self):
        """Test inputs that are not numeric."""
        invalid_inputs = ["eighty", "A+", None, [90], {"score": 90}]
        for item in invalid_inputs:
            with self.subTest(item=item):
                with self.assertRaises(TypeError):
                    assign_grade(item)

if __name__ == '__main__':
    # This allows running the tests directly from the command line
    unittest.main(verbosity=2)
