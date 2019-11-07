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
 
    def test_population_correlation_coefficient(self):
        test_data = CsvReader('/Tests/Data/unit_test_population_correlation_coefficient.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.population_correlation_coefficient(row['Value 1'],row['Value 2'],row['Value 3']), Decimal(row['Result']).quantize(Decimal('.001')))
            self.assertEqual(self.calculator.result, Decimal(row['Result']).quantize(Decimal('.001')))

    def test_confidence_interval(self):
        test_data = CsvReader('/Tests/Data/unit_test_confidence_interval.csv').data
        for row in test_data:
            self.assertEqual(
                self.calculator.confidence_interval(row['Value 1'], row['Value 2'], row['Value 3']),
                Decimal(row['Result']).quantize(Decimal('.001')))
            self.assertEqual(self.calculator.result, Decimal(row['Result']).quantize(Decimal('.001')))

    def test_population_variance(self):
        test_data = CsvReader('/Tests/Data/unit_test_population_variance.csv').data
        for row in test_data:
            self.assertEqual(
                self.calculator.population_variance(row['Value 1'], row['Value 2'], row['Value 3']),
                Decimal(row['Result']).quantize(Decimal('.001')))
            self.assertEqual(self.calculator.result, Decimal(row['Result']).quantize(Decimal('.001')))

    def test_p_value(self):
        test_data = CsvReader('/Tests/Data/unit_test_p_value.csv').data
        for row in test_data:
            self.assertEqual(
                self.calculator.p_value(row['Value 1'], row['Value 2'], row['Value 3']),
                Decimal(row['Result']).quantize(Decimal('.001')))
            self.assertEqual(self.calculator.result, Decimal(row['Result']).quantize(Decimal('.001')))

    def test_proportion(self):
        test_data = CsvReader('/Tests/Data/unit_test_proportion.csv').data
        for row in test_data:
            self.assertEqual(
                self.calculator.proportion(row['Value 1'], row['Value 2'], row['Value 3'], row['Value 4']),
                Decimal(row['Result']).quantize(Decimal('.001')))
            self.assertEqual(self.calculator.result, Decimal(row['Result']).quantize(Decimal('.001')))

    def test_sample_mean(self):
        test_data = CsvReader('/Tests/Data/unit_test_sample_mean.csv').data
        for row in test_data:
            self.assertEqual(
                self.calculator.sample_mean(row['Value 1'], row['Value 2'], row['Value 3']),
                Decimal(row['Result']).quantize(Decimal('.001')))
            self.assertEqual(self.calculator.result, Decimal(row['Result']).quantize(Decimal('.001')))

    def test_sample_standard_deviation(self):
        test_data = CsvReader('/Tests/Data/unit_test_sample_standard_deviation.csv').data
        for row in test_data:
            self.assertEqual(
                self.calculator.sample_standard_deviation(row['Value 1'], row['Value 2'], row['Value 3']),
                Decimal(row['Result']).quantize(Decimal('.001')))
            self.assertEqual(self.calculator.result, Decimal(row['Result']).quantize(Decimal('.001')))

    def test_variance_of_sample_proportion(self):
        test_data = CsvReader('/Tests/Data/unit_test_variance_of_sample_proportion.csv').data
        for row in test_data:
            self.assertEqual(
                self.calculator.variance_of_sample_proportion(row['Value 1'], row['Value 2'], row['Value 3']),
                Decimal(row['Result']).quantize(Decimal('.001')))
            self.assertEqual(self.calculator.result, Decimal(row['Result']).quantize(Decimal('.001')))

if __name__ == '__main__':
    unittest.main()