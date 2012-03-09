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

class RomanTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(roman(1), "I")

    def test_2(self):
        self.assertEqual(roman(2), "II")

    def test_3(self):
        self.assertEqual(roman(3), "III")

    def test_4(self):
        self.assertEqual(roman(4), "IV")

    def test_5(self):
        self.assertEqual(roman(5), "V")

    def test_6(self):
        self.assertEqual(roman(6), "VI")

    def test_7(self):
        self.assertEqual(roman(7), "VII")

    def test_8(self):
        self.assertEqual(roman(8), "VIII")

    def test_9(self):
        self.assertEqual(roman(9), "IX")

    def test_10(self):
        self.assertEqual(roman(10), "X")

def roman(num):
    if num < 4:
        return "I" * num

    if num == 4:
        return "IV"

    if num == 5:
        return "V"

def main():
    unittest.main()

if __name__ == '__main__':
    main()