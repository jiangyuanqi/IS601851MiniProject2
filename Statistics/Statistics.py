import math

class Statistics:
    def __init__(self):
        pass

    def add(self,nums):
        return sum(nums)

    def count(self,nums):
        return len(nums)

    def mean(self,nums):
        return self.population_mean(nums)


    def population_mean(self,nums):
        return self.add(nums)/self.count(nums)    

    def median(self,nums):
        if len(nums)%2==1:
            return sorted(nums)[int(len(nums)/2)]
        else:
            return self.mean(sorted(nums)[int(len(nums)/2)-1:int(len(nums)/2)+1])

    def mode(self,nums):
        count=nums.count(max(nums, key=nums.count))
        return sorted([int(num) for num in set(nums) if nums.count(num)==count])

    def population_stdev(self,nums):
        return math.sqrt(self.population_variance(nums))

    def population_variance(self,nums,):
        return self.mean([(num-self.mean(nums))**2 for num in nums])

    def zscore(self,nums, sample):
        return (sample-self.mean(nums))/self.population_stdev(nums)

    def standardized_score(self,nums, sample):
        return self.zscore(nums,sample)

    def population_correlation_coefficient(self,numsx, numsy):
        return self.mean([(numsx[idx]-self.mean(numsx))*(numsy[idx]-self.mean(numsy)) for idx, num in enumerate(numsx)])/(self.population_stdev(numsx)*self.population_stdev(numsy))

    #this function will calculate a 95% confidence interval for the mean of a large sample size
    def confidence_interval(self,nums, sampleMean):
        marginOfError=1.96*(sampleMean/math.sqrt(self.count(nums)))
        return (sampleMean-marginOfError,sampleMean+marginOfError)

    def p_value(self,nums, hypothesisMean, populationStdev):
        return (self.sample_mean(nums)-hypothesisMean)/(populationStdev/math.sqrt(self.count(nums)))

    def proportion(self,a, b):
        return a/b

    def sample_mean(self,nums):
        return self.population_mean(nums)

    def sample_standard_deviation(self,nums):
        return math.sqrt(self.variance_of_sample_proportion(nums))

    def variance_of_sample_proportion(self,nums):
        return self.population_variance(nums)*self.count(nums)/(self.count(nums)-1)

