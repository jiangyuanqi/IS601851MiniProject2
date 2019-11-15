import unittest
import math
from decimal import Decimal
from Calculator.Calculator import Calculator
from CsvReader.CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_mean(self):
        test_data = CsvReader('./Tests/Data/unit_test_mean.csv').data
        for row in test_data:
            nums = [int(val) for val in row['nums'].split('_')]
            result = int(row['result'])
            self.assertEqual(self.calculator.population_mean(nums), result)
            self.assertEqual(self.calculator.result, result)
            self.assertNotEqual(self.calculator.population_mean(nums), result-1)
            self.assertNotEqual(self.calculator.result, result-1)

    def test_median(self):
        test_data = CsvReader('./Tests/Data/unit_test_median.csv').data
        for row in test_data:
            nums = [float(val) for val in row['nums'].split('_')]
            result = float(row['result'])
            self.assertEqual(self.calculator.median(nums), result)
            self.assertEqual(self.calculator.result, result)
            self.assertNotEqual(self.calculator.median(nums), result-1)
            self.assertNotEqual(self.calculator.result, result-1)
            
    def test_mode(self):
        test_data = CsvReader('./Tests/Data/unit_test_mode.csv').data
        for row in test_data:
            nums = [float(val) for val in row['nums'].split('_')]
            result = [float(val) for val in row['result'].split('_') if val != '']
            self.assertEqual(self.calculator.mode(nums), result)
            self.assertEqual(self.calculator.result, result)
            if len(result) !=0:#add some other number so we can check if the mode is not equal
                result.append(result[0])
            else:
                result.append(0)
            self.assertNotEqual(self.calculator.mode(nums), result)
            self.assertNotEqual(self.calculator.result, result)

    def test_sample_standard_deviation(self):
        test_data = CsvReader('./Tests/Data/unit_test_sample_standard_deviation.csv').data
        for row in test_data:
            nums = [float(val) for val in row['nums'].split('_')]
            result = float(row['result'])
            self.assertAlmostEqual(self.calculator.sample_standard_deviation(nums), result)
            self.assertAlmostEqual(self.calculator.result, result)
            self.assertNotEqual(self.calculator.sample_standard_deviation(nums), result-1)
            self.assertNotEqual(self.calculator.result, result-1)

    def test_population_variance(self):
        test_data = CsvReader('./Tests/Data/unit_test_population_variance.csv').data
        for row in test_data:
            nums = [float(val) for val in row['nums'].split('_')]
            result = float(row['result'])
            self.assertAlmostEqual(self.calculator.population_variance(nums), result)
            self.assertAlmostEqual(self.calculator.result, result)
            self.assertNotEqual(self.calculator.population_variance(nums), result-1)
            self.assertNotEqual(self.calculator.result, result-1)

    def test_zscore(self):
        test_data = CsvReader('./Tests/Data/unit_test_zscore.csv').data
        for row in test_data:
            nums = [float(val) for val in row['nums'].split('_')]
            sample = float(row['sample'])
            result = float(row['result'])
            self.assertAlmostEqual(self.calculator.zscore(nums, sample), result)
            self.assertAlmostEqual(self.calculator.result, result)
            self.assertNotEqual(self.calculator.zscore(nums, sample), result-1)
            self.assertNotEqual(self.calculator.result, result-1)
"""
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
"""
if __name__ == '__main__':
    unittest.main()