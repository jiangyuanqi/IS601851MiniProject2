import math
from decimal import Decimal
import statistics

def add(nums):
    return sum(nums)

def count(nums):
    return len(nums)

def population_mean(nums):
    return add(nums)/count(nums)

def median(nums):
    if len(nums)%2==1:
        return sorted(nums)[int(len(nums)/2)]
    else:
        return population_mean(sorted(nums)[int(len(nums)/2)-1:int(len(nums)/2)+1])

def mode(nums):
    count=nums.count(max(nums, key=nums.count))
    return sorted([int(num) for num in set(nums) if nums.count(num)==count])

def population_stdev(nums):
    return math.sqrt(population_variance(nums))

def population_variance(nums,):
    return mean([(num-mean(nums))**2 for num in nums])

def zscore(nums, sample):
    return (sample-mean(nums))/population_stdev(nums)

def standardized_score(nums, sample):
    return zscore(nums,sample)

def population_correlation_coefficient(numsx, numsy):
    return mean([(numsx[idx]-mean(numsx))*(numsy[idx]-mean(numsy)) for idx, num in enumerate(numsx)])/(stdev(numsx)*stdev(numsy))

#this function will calculate a 95% confidence interval for the mean of a large sample size
def confidence_interval(nums, sampleMean):
    marginOfError=1.96*(sampleMean/math.sqrt(count(nums)))
    return (sampleMean-marginOfError,sampleMean+marginOfError)

def p_value(nums, hypothesisMean, populationMean, populationStdev):
    return (sample_mean(nums)-hypothesisMean)/(populationStdev/math.sqrt(count(nums)))

def proportion(a, b):
    return a/b

def sample_mean(nums):
    return population_mean(nums)

def sample_standard_deviation(nums):
    return math.sqrt(variance_of_sample_proportion(nums))

def variance_of_sample_proportion(nums):
    return population_variance(nums)*count(nums)/(count(nums)-1)

class Calculator:
    result = 0

    def __init__(self):
        pass

    def population_mean(self, nums):
        self.result = population_mean(nums)
        return self.result

    def median(self, nums):
        self.result = median(nums)
        return self.result

    def mode(self, nums):
        self.result = mode(nums)
        return self.result

    def population_stdev(self, nums):
        self.result = population_stdev(nums)
        return self.result

    def population_variance(self, nums):
        self.result = population_variance(nums)
        return self.result

    def zscore(self, nums, sample):
        self.result = zscore(nums, sample)
        return self.result

    def standardized_score(self, nums, sample):
        self.result = standardized_score(nums, sample)
        return self.result

    def population_correlation_coefficient(self, numsx, numsy):
        self.result = population_correlation_coefficient(numsx, numsy)
        return self.result

    def confidence_interval(self, nums, sampleMean):
        self.result = confidence_interval(nums, sampleMean)
        return self.result

    def p_value(self, nums, hypothesisMean, populationMean, populationStdev):
        self.result = p_value(nums, hypothesisMean, populationMean, populationStdev)
        return self.result

    def proportion(self, a, b):
        self.result = proportion(a, b)
        return self.result

    def sample_mean(self, nums):
        self.result = sample_mean(nums)
        return self.result

    def sample_standard_deviation(self, nums):
        self.result = sample_standard_deviation(nums)
        return self.result

    def variance_of_sample_proportion(self, nums):
        self.result = variance_of_sample_proportion(nums)
        return self.result
