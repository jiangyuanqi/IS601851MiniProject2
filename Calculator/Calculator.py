import math
from decimal import Decimal
import statistics

def add(nums):
    nums = [num for num in nums]
    return sum(nums)

def count(nums):
    return len(nums)

def mean(nums):
    return add(nums)/count(nums)

def median(nums):
    if len(nums)%2==1:
        return sorted(nums)[int(len(nums)/2)]
    else:
        return mean(sorted(nums)[int(len(nums)/2)-1:int(len(nums)/2)+1])

def mode(nums):
    count=nums.count(max(nums, key=nums.count))
    return sorted([int(num) for num in set(nums) if nums.count(num)==count])

def stdev(nums):
    return math.sqrt(variance(nums))

def variance(nums,):
    return mean([(num-mean(nums))**2 for num in nums])

def zscore(nums, sample):
    return (sample-mean(nums))/stdev(nums)

def standardized_score(nums, sample):
    return zscore(nums,sample)

def population_correlation_coefficient(numsx, numsy):
    return mean([(numsx[idx]-mean(numsx))*(numsy[idx]-mean(numsy)) for idx, num in enumerate(numsx)])/(stdev(numsx)*stdev(numsy))

def confidence_interval(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    d = zscore(a, b, c)
    e = stdev(a, b, c)
    f = d * e / Decimal(math.sqrt(3)).quantize(Decimal('.001'))
    return Decimal(f).quantize(Decimal('.001'))

def population_variance(nums):
    return variance(nums)

def p_value(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    d = stdev(a, b, c)
    e = 2 * abs(d)
    return Decimal(e).quantize(Decimal('.001'))

def proportion(a, b):
    return a/b

def sample_mean(nums):
    return mean(nums)

def sample_standard_deviation(nums):
    return math.sqrt(variance_of_sample_proportion(nums))

def variance_of_sample_proportion(nums):
    return variance(nums)*count(nums)/(count(nums)-1)

class Calculator:
    result = 0

    def __init__(self):
        pass

    def mean(self, nums):
        self.result = mean(nums)
        return self.result

    def median(self, nums):
        self.result = median(nums)
        return self.result

    def mode(self, nums):
        self.result = mode(nums)
        return self.result

    def stdev(self, nums):
        self.result = stdev(nums)
        return self.result

    def variance(self, nums):
        self.result = variance(nums)
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

    def confidence_interval(self, a, b, c):
        self.result = confidence_interval(a, b, c)
        return self.result

    def population_variance(self, nums):
        self.result = population_variance(nums)
        return self.result

    def p_value(self, a, b, c):
        self.result = p_value(a, b, c)
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
