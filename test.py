import unittest
import functions as two

"""
here is a template test that you can use to write test cases for the code you write
to run this test run 'python test.py' and you'll see the below test passes
"""

class Test_Example(unittest.TestCase):
    # this test checks if the function bark3() in the 'functions' python script works correctly
    def test_functions_bark3(self):
        self.assertEqual(two.bark3(), 'The hound barked!') # assert that 'two.bark3()' returns the "The hound barked!"

    def test_a_table_test(self):
        # here we are iterating through a series of tests and testing them all one by one
        # useful when you have to test multiple conditions for one function or set of functions
        tests = {
            "test1": {
                "value1": 9,
                "value2": 2,
            },
            "test2": {
                "value1": 6,
                "value2": 3,
            },
        }
        for key in tests:
            # does each test value1*value2 equal 18?
            self.assertEqual(tests[key]["value1"]*tests[key]["value2"], 18, key)

if __name__ == '__main__':
    unittest.main()