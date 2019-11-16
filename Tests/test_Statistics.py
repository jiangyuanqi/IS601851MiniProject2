import unittest
import math
from decimal import Decimal
from Statistics.Statistics import Statistics as statistic
from CsvReader.CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistic = statistic()

    def test_mean(self):
        test_data = CsvReader('./Tests/Data/unit_test_mean.csv').data
        for row in test_data:
            nums = [float(val) for val in row['nums'].split('_')]
            result = float(row['result'])
            self.assertAlmostEqual(self.statistic.population_mean(nums), result)
            self.assertNotEqual(self.statistic.population_mean(nums), result-1)

    def test_median(self):
        test_data = CsvReader('./Tests/Data/unit_test_median.csv').data
        for row in test_data:
            nums = [float(val) for val in row['nums'].split('_')]
            result = float(row['result'])
            self.assertAlmostEqual(self.statistic.median(nums), result)
            self.assertNotEqual(self.statistic.median(nums), result-1)
            
    def test_mode(self):
        test_data = CsvReader('./Tests/Data/unit_test_mode.csv').data
        for row in test_data:
            nums = [float(val) for val in row['nums'].split('_')]
            result = [float(val) for val in row['result'].split('_') if val != '']
            self.assertAlmostEqual(self.statistic.mode(nums), result)
            if len(result) !=0:#add some other number so we can check if the mode is not equal
                result.append(result[0])
            else:
                result.append(0)
            self.assertNotEqual(self.statistic.mode(nums), result)

    def test_sample_standard_deviation(self):
        test_data = CsvReader('./Tests/Data/unit_test_sample_standard_deviation.csv').data
        for row in test_data:
            nums = [float(val) for val in row['nums'].split('_')]
            result = float(row['result'])
            self.assertAlmostEqual(self.statistic.sample_standard_deviation(nums), result)
            self.assertNotEqual(self.statistic.sample_standard_deviation(nums), result-1)

    def test_population_standard_deviation(self):
        test_data = CsvReader('./Tests/Data/unit_test_population_standard_deviation.csv').data
        for row in test_data:
            nums = [float(val) for val in row['nums'].split('_')]
            result = float(row['result'])
            self.assertAlmostEqual(self.statistic.population_stdev(nums), result)
            self.assertNotEqual(self.statistic.population_stdev(nums), result-1)

    def test_population_variance(self):
        test_data = CsvReader('./Tests/Data/unit_test_population_variance.csv').data
        for row in test_data:
            nums = [float(val) for val in row['nums'].split('_')]
            result = float(row['result'])
            self.assertAlmostEqual(self.statistic.population_variance(nums), result)
            self.assertNotEqual(self.statistic.population_variance(nums), result-1)

    def test_zscore(self):
        test_data = CsvReader('./Tests/Data/unit_test_zscore.csv').data
        for row in test_data:
            nums = [float(val) for val in row['nums'].split('_')]
            sample = float(row['sample'])
            result = float(row['result'])
            self.assertAlmostEqual(self.statistic.zscore(nums, sample), result)
            self.assertNotEqual(self.statistic.zscore(nums, sample), result-1)

    def test_standardized_score(self):
        test_data = CsvReader('./Tests/Data/unit_test_standardized_score.csv').data
        for row in test_data:
            nums = [float(val) for val in row['nums'].split('_')]
            sample = float(row['sample'])
            result = float(row['result'])
            self.assertAlmostEqual(self.statistic.zscore(nums, sample), result)
            self.assertNotEqual(self.statistic.zscore(nums, sample), result-1)

    def test_population_correlation_coefficient(self):
        test_data = CsvReader('./Tests/Data/unit_test_population_correlation_coefficient.csv').data
        for row in test_data:
            numsx = [float(val) for val in row['numsx'].split('_')]
            numsy = [float(val) for val in row['numsy'].split('_')]
            result = float(row['result'])
            self.assertAlmostEqual(self.statistic.population_correlation_coefficient(numsx, numsy), result)
            self.assertNotEqual(self.statistic.population_correlation_coefficient(numsx, numsy), result-1)

    def test_confidence_interval(self):
        test_data = CsvReader('./Tests/Data/unit_test_confidence_interval.csv').data
        for row in test_data:
            nums = [float(val) for val in row['nums'].split('_')]
            sampleMean = float(row['sampleMean'])
            result = [float(val) for val in row['result'].split('_')]
            val = self.statistic.confidence_interval(nums, sampleMean)
            self.assertAlmostEqual(val[0], result[0])
            self.assertAlmostEqual(val[1], result[1])
            self.assertNotEqual(val[0], result[0]-1)
            self.assertNotEqual(val[1], result[1]-1)
            

    def test_p_value(self):
        test_data = CsvReader('./Tests/Data/unit_test_p_value.csv').data
        for row in test_data:
            nums = [float(val) for val in row['nums'].split('_')]
            hypothesisMean = float(row['hypothesisMean'])
            populationStdev = float(row['populationStdev'])
            result = float(row['result'])
            self.assertAlmostEqual(self.statistic.p_value(nums, hypothesisMean, populationStdev), result)
            self.assertNotEqual(self.statistic.p_value(nums, hypothesisMean, populationStdev), result-1)

    def test_proportion(self):
        test_data = CsvReader('./Tests/Data/unit_test_proportion.csv').data
        for row in test_data:
            a = float(row['a'])
            b = float(row['b'])
            result = float(row['result'])
            self.assertAlmostEqual(self.statistic.proportion(a, b), result)
            self.assertNotEqual(self.statistic.proportion(a, b), result-1)

    def test_sample_mean(self):
        test_data = CsvReader('./Tests/Data/unit_test_sample_mean.csv').data
        for row in test_data:
            nums = [float(val) for val in row['nums'].split('_')]
            result = float(row['result'])
            self.assertAlmostEqual(self.statistic.population_mean(nums), result)
            self.assertNotEqual(self.statistic.population_mean(nums), result-1)

    def test_variance_of_sample_proportion(self):
        test_data = CsvReader('./Tests/Data/unit_test_variance_of_sample_proportion.csv').data
        for row in test_data:
            nums = [float(val) for val in row['nums'].split('_')]
            result = float(row['result'])
            self.assertAlmostEqual(self.statistic.variance_of_sample_proportion(nums), result)
            self.assertNotEqual(self.statistic.variance_of_sample_proportion(nums), result-1)
   
    def test_variance_of_population_proportion(self):
        test_data = CsvReader('./Tests/Data/unit_test_variance_of_population_proportion.csv').data
        for row in test_data:
            nums = [float(val) for val in row['nums'].split('_')]
            result = float(row['result'])
            self.assertAlmostEqual(self.statistic.variance_of_population_proportion(nums), result)
            self.assertNotEqual(self.statistic.variance_of_population_proportion(nums), result-1)

if __name__ == '__main__':
    unittest.main()