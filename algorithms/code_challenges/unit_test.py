import unittest
from random import shuffle
from first_positive_missing import first_positive_number_missing_optimal


class TestCase(unittest.TestCase):
    def test_first_positive_number_missing(self):
        test_case = list(range(100))
        for i in range(1, 100):
            curr_test_case = test_case.copy()
            target_result = curr_test_case[i]
            curr_test_case.remove(i)
            curr_test_case.extend([-1] * 10)
            shuffle(curr_test_case)
            result = first_positive_number_missing_optimal(curr_test_case)
            self.assertEqual(result, target_result)


if __name__ == '__main__':
    unittest.main()
