import unittest
import math
from decimal import Decimal
from Calculator.Calculator import Calculator
from CsvReader.CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_mean(self):
        test_data = CsvReader('/Tests/Data/unit_test_mean.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.mean(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))


    def test_median(self):
        test_data = CsvReader('/Tests/Data/unit_test_median.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.median(row['Value 1'],row['Value 2'],row['Value 3']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_mode(self):
        test_data = CsvReader('/Tests/Data/unit_test_mode.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.mode(row['Value 1'],row['Value 2'],row['Value 3']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_stdev(self):
        test_data = CsvReader('/Tests/Data/unit_test_stdev.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.stdev(row['Value 1'],row['Value 2'],row['Value 3']), Decimal(row['Result']).quantize(Decimal('.001')))
            self.assertEqual(self.calculator.result, Decimal(row['Result']).quantize(Decimal('.001')))

    def test_variance(self):
        test_data = CsvReader('/Tests/Data/unit_test_variance.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.variance(row['Value 1'],row['Value 2'],row['Value 3']), Decimal(row['Result']).quantize(Decimal('.001')))
            self.assertEqual(self.calculator.result, Decimal(row['Result']).quantize(Decimal('.001')))


    def test_zscore(self):
        test_data = CsvReader('/Tests/Data/unit_test_zscore.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.zscore(row['Value 1'],row['Value 2'],row['Value 3']), Decimal(row['Result']).quantize(Decimal('.001')))
            self.assertEqual(self.calculator.result, Decimal(row['Result']).quantize(Decimal('.001')))

    def test_standardized_score(self):
        test_data = CsvReader('/Tests/Data/unit_test_standardized_score.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.standardized_score(row['Value 1'],row['Value 2'],row['Value 3']), Decimal(row['Result']).quantize(Decimal('.001')))
            self.assertEqual(self.calculator.result, Decimal(row['Result']).quantize(Decimal('.001')))


 '''


Confidence Interval
Population Variance
P Value
Proportion
Sample Mean
Sample Standard Deviation
Variance of sample proportion
'''

if __name__ == '__main__':
    unittest.main()