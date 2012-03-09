#coding: utf-8

"""
Convert arabic numbers into roman numbers.

Test Cases

roman(1) -> I
roman(2) -> II
roman(3) -> III
roman(4) -> IV
roman(5) -> V
roman(6) -> VI
roman(7) -> VII
roman(8) -> VIII
roman(9) -> IX
roman(10) -> X
roman(50) -> L
roman(500) -> D
roman(1000) -> M

"""
import unittest

def roman(num):
    if num == 1:
        return "I"

class RomanTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(roman(1), "I")

def main():
    unittest.main()

if __name__ == '__main__':
    main()