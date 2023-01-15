import unittest
import solution

class Test_ExampleSolution(unittest.TestCase):
    def test_example_solution(self):
        testcases = {
            1: {'ALEX': {39}, 'ROSIE': {38}, 'JOHN': {33}},
            2: {'ALEX': {16}, 'TIM': {17}, 'TOM': {12}},
            3: {'ALEX': {2}, 'TIM': {1}, 'TOM': {8}},
        }
        for key in testcases:
            self.assertEqual(solution.highscore('challenge1.csv', key), testcases[key])

if __name__ == '__main__':
    unittest.main()