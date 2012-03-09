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

    def test_16(self):
        self.assertEqual(roman(16), "XVI")    

    def test_50(self):
        self.assertEqual(roman(50), "L")

    def test_500(self):
        self.assertEqual(roman(500), "D")

    def test_1000(self):
        self.assertEqual(roman(1000), "M")

test = False

def roman(num):
    units = [
        [1,"I"]
        , [5, "V"]
        , [10, "X"]
        , [50, "L"]
        , [500, "D"]
        , [1000, "M"]
    ]

    def get_limit_unit(n):
        return filter(lambda unit: n + 1 >= unit[0], units)

    limit = get_limit_unit(num)

    multiplier = num % 5
    if test:
        print limit, num, multiplier

    if multiplier == 0:
        last = limit[-1]
        return last[1] * (num/last[0])
    elif multiplier < 4 :
        if len(limit) == 1:
            return limit[0][1] * multiplier
        elif len(limit) > 2:
            first = limit.pop(0)
            limit.reverse()
            return limit[0][1] + limit[-1][1] + first[1] * multiplier
        limit.reverse()
        return limit[0][1] + limit[-1][1] * multiplier    
    elif multiplier == 4:
        last = limit.pop()
        return limit[0][1] + last[1]

def main():
    if test:
        for x in range(15, 21):
            print roman(x)    
    else:
        unittest.main()
    


if __name__ == '__main__':
    main()