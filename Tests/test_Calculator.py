import unittest
import math
from decimal import Decimal
from Calculator.Calculator import Calculator
from CsvReader.CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_square_root(self):
        test_data = CsvReader('/Tests/Data/Unit Test Square Root.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.square_root(row['Value 1']),
                             Decimal(row['Result']).quantize(Decimal('.000001')))
            self.assertEqual(self.calculator.result, Decimal(row['Result']).quantize(Decimal('.000001')))

    def test_square(self):
        test_data = CsvReader('/Tests/Data/Unit Test Square.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.square(row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_division(self):
        test_data = CsvReader('/Tests/Data/Unit Test Division.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.division(row['Value 1'], row['Value 2']), Decimal(row['Result']))
            self.assertEqual(self.calculator.result, Decimal(row['Result']))

    def test_multiplication(self):
        test_data = CsvReader('/Tests/Data/Unit Test Multiplication.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.multiplication(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_subtract(self):
        test_data = CsvReader('/Tests/Data/Unit Test Subtraction.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_addition(self):
        test_data = CsvReader('/Tests/Data/Unit Test Addition.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.add(row['Value 2'], row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))


if __name__ == '__main__':
    unittest.main()