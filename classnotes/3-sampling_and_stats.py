# Basic random sampling and statistics (mean, stdev)

import random
import statistics as stats   # Common module for basic stats functions

# Sample data set, [1,1000]
data = list(range(1,1001))
#print(data)

# Sets the "seed" to 1. All results will be consistent.
random.seed(1)

# Sample 30 random numbers (without replacement)
# samp = random.sample(data, k=10)

# Sample 30 random numbers (with replacement)
samp = random.choices(data, k=30)

# Print the mean and standard deviation (population and sample)
print(stats.mean(samp))
print(stats.pstdev(samp))
print(stats.stdev(samp))
