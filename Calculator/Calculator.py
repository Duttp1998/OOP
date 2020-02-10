from MathOperations.addition import Addition
from MathOperations.subtraction import Subtraction
from MathOperations.multiplication import Multiplication
from MathOperations.division import Division
from MathOperations.exponentiation import Exponentiation
from MathOperations.root import Root
from MathOperations.logarithm import Logarithm


class Calculator:
    Result = 0

    def __init__(self):
        pass

    def Sum(self, a, b):
        self.Result = Addition.sum(a, b)
        return self.Result

    def Difference(self, a, b):
        self.Result = Subtraction.difference(a, b)
        return self.Result

    def Product(self, a, b):
        self.Result = Multiplication.product(a, b)
        return self.Result

    def Fraction(self, a, b):
        self.Result = Division.fraction(a, b)
        return self.Result

    def Power(self, a, b):
        self.Result = Exponentiation.power(a, b)
        return self.Result

    def Root(self, a, b):
        self.Result = Root.root(a, b)
        return self.Result

    def logarithm(self, a, b):
        self.Result = Logarithm.logarithm(a, b)
        return self.Result
