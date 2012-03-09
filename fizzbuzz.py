#coding: utf-8

"""
    Return “fizz”, “buzz” or “fizzbuzz”.

    For a given natural number greater zero return

    * “fizz” if the number is dividable by 3
    * “buzz” if the number is dividable by 5
    * “fizzbuzz” if the number is dividable by 15

    Test Cases
    ----------
    Input   Result
    1       1
    2       2
    3       fizz
    4       4
    5       buzz
    6       fizz
    10      buzz
    15      fizzbuzz
"""

import unittest

def fizzbuzz(n):

    result = n
    if n % 3 == 0:
        result = "fizz"

    if n % 5 == 0:
        if result == "fizz":
            return "%sbuzz" % result
        result = "buzz"

    return result

class fizzbuzzTests(unittest.TestCase):
    def test_chiffre(self):
        self.assertEqual(fizzbuzz(1), 1)
        self.assertEqual(fizzbuzz(2), 2)
        self.assertEqual(fizzbuzz(4), 4)

    def test_fizz(self):
        self.assertEqual(fizzbuzz(3), "fizz")
        self.assertEqual(fizzbuzz(6), "fizz")

    def test_buzz(self):
        self.assertEqual(fizzbuzz(5), "buzz")
        self.assertEqual(fizzbuzz(10), "buzz")

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15), "fizzbuzz")
        
def main():
    unittest.main()

if __name__ == '__main__':
    main()

