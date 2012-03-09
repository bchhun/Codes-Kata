#coding: utf-8
"""
Compute the prime factors of a given natural number.

Bernard says: What is a prime factor ? http://en.wikipedia.org/wiki/Prime_factor

Test Cases ([...] denotes a list)

primes(1) -> []
primes(2) -> [2]
primes(3) -> [3]
primes(4) -> [2,2]
primes(5) -> [5]
primes(6) -> [2,3]
primes(7) -> [7]
primes(8) -> [2,2,2]
primes(9) -> [3,3]
"""

import unittest, math

def is_prime(num):
    """
        http://en.wikipedia.org/wiki/Prime_number
    """
    i = 2
    while i <= math.sqrt(num):
        if num % i == 0:
            return False
        i += 1
    return True

def primes(num):
    primes_list = []
    base = 2
    possibilities = xrange(base, num+1)
    possibility = base

    while (not primes_list) and (possibility in possibilities):
        if is_prime(possibility) and num%possibility == 0:
            primes_list = primes_list + [possibility] + primes(num/possibility)
        possibility += 1
    return primes_list

class primesTest(unittest.TestCase):

    def test_unique(self):
        self.assertEqual(primes(1), [])
        self.assertEqual(primes(2), [2])
        self.assertEqual(primes(3), [3])     
        self.assertEqual(primes(5), [5])
        self.assertEqual(primes(7), [7])

    def test_multiple(self):
        self.assertEqual(primes(4), [2,2])   
        self.assertEqual(primes(6), [2,3])
        self.assertEqual(primes(8), [2,2,2])
        self.assertEqual(primes(9), [3,3])

def main():
    unittest.main()

if __name__ == '__main__':
    main()