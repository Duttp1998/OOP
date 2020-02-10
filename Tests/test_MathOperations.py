import unittest

from MathOperations.addition import Addition
from MathOperations.subtraction import Subtraction
from MathOperations.multiplication import Multiplication
from MathOperations.division import Division
from MathOperations.exponentiation import Exponentiation
from MathOperations.root import Root
from MathOperations.logarithm import Logarithm


class MyTestCase(unittest.TestCase):

    def test_MathOperations_Addition(self):
        self.assertEqual(3, Addition.sum(1, 2))

    def test_MathOperations_subtraction(self):
        self.assertEqual(-1, Subtraction.difference(1, 2))

    def test_MathOperations_multiplication(self):
        self.assertEqual(2, Multiplication.product(1, 2))

    def test_MathOperations_division(self):
        self.assertEqual(2, Division.fraction(4, 2))

    def test_MathOperations_exponentiation(self):
        self.assertEqual(4, Exponentiation.power(2, 2))

    def test_MathOperations_root(self):
        self.assertEqual(8.54400374531753, Root.root(8, 3))

    def test_MathOperations_logarithm(self):
        self.assertEqual(2, Logarithm.logarithm(3, 6))

    def test_MathOperations_sum_list(self):
        valuelist = [1, 2, 3]
        self.assertEqual(6, Addition.sum(valuelist))



if __name__ == '__main__':
    unittest.main()
