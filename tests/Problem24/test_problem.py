import unittest

from problems.Problem24.problem import get_nth_permutation


class TestsProblem24(unittest.TestCase):

    def test_get_nth_permutation_for_millionth_permutation_returns_2783915460(self):
        result = get_nth_permutation(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 100_000_0)
        self.assertEqual('2783915460', result)


if __name__ == '__main__':
    unittest.main()
