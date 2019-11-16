from Statistics.Statistics import Statistics as statistic

class Calculator:
    result = 0
    stat = statistic()
    def __init__(self):
        pass

    def population_mean(self, nums):
        self.result = self.stat.population_mean(nums)
        return self.result

    def median(self, nums):
        self.result = self.stat.median(nums)
        return self.result

    def mode(self, nums):
        self.result = self.stat.mode(nums)
        return self.result

    def population_stdev(self, nums):
        self.result = self.stat.population_stdev(nums)
        return self.result

    def population_variance(self, nums):
        self.result = self.stat.population_variance(nums)
        return self.result

    def zscore(self, nums, sample):
        self.result = self.stat.zscore(nums, sample)
        return self.result

    def standardized_score(self, nums, sample):
        self.result = self.stat.standardized_score(nums, sample)
        return self.result

    def population_correlation_coefficient(self, numsx, numsy):
        self.result = self.stat.population_correlation_coefficient(numsx, numsy)
        return self.result

    def confidence_interval(self, nums, sampleMean):
        self.result = self.stat.confidence_interval(nums, sampleMean)
        return self.result

    def p_value(self, nums, hypothesisMean, populationStdev):
        self.result = self.stat.p_value(nums, hypothesisMean, populationStdev)
        return self.result

    def proportion(self, a, b):
        self.result = self.stat.proportion(a, b)
        return self.result

    def sample_mean(self, nums):
        self.result = self.stat.sample_mean(nums)
        return self.result

    def sample_standard_deviation(self, nums):
        self.result = self.stat.sample_standard_deviation(nums)
        return self.result

    def variance_of_sample_proportion(self, nums):
        self.result = self.stat.variance_of_sample_proportion(nums)
        return self.result
