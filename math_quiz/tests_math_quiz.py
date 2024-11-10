import unittest
from math_quiz import generate_integer, generate_operator, math_example_result


class TestMathGame(unittest.TestCase):

    def test_generate_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = -10
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_generate_operator(self):
        # Test if generator for operator returns one of expected ones.
        operators_set = {"+","-","*"}
        for _ in range(1000):   # Test a large number of generated operators.
             rand_operator = generate_operator()
             self.assertTrue(rand_operator in operators_set) 

    def test_math_example_result(self):
        # Test if function for generating math problems and calculating their results work.
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (-10, -10, '-', '-10 - (-10)', 0),
                (0, 9, '*', '0 * 9', 0),
                (7, -4, '+', '7 + (-4)', 3),
                (4, 8, '-', '4 - 8', -4),
                (6, -3, '*', '6 * (-3)', -18)
            ]
            
            for num1, num2, operator, expected_problem, expected_answer in test_cases:  # Test for all test_cases
                problem, result = math_example_result(num1, num2, operator)
                self.assertTrue(problem == expected_problem and result == expected_answer)

if __name__ == "__main__":
    unittest.main()
