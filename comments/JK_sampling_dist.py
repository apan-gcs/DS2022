"""
Ms Pan's Comments: Some minor notes:
- Deleted some comments originally from my code
- Protip: Line up comments when you can (see samples / n, mean / stderr)
- x-label is more accurate as mean or average height, or sample mean of heights.
- Edited annotation since it was slightly to close to the edge.
  Could even be on the left side.
"""


"""
Joan Keane
September 27, 2022

Q1 Mini Project - Sampling Distribution
"""

from pandas import read_csv
import random
from matplotlib import pyplot as plt
import statistics as stats 

# Importing data as a DataFrame
# Then converting in to a regular list
filename = "heights.csv"
data = read_csv(filename, header=None)
data = data[0].values.tolist()

# Sets the "seed" to 1. All results will be consistent.
random.seed(1)

samples = 1000  # Number of sample
n = 30          # Sample size

dist = []
heights = []

# Random sampling
for i in range(samples):
    heights = random.sample(data, k = n)
    samp_mean = stats.mean(heights)
    dist.append(samp_mean)
    
av = (stats.mean(dist))        # Sampling distribution mean
std_er = (stats.pstdev(dist))  # Standard error


# Plot a histogram
plt.hist(dist, bins = 20, rwidth = 0.9)

# Edit title and axes
plt.title("Sampling Distribution of Heights (12-13 Year-olds)", fontsize = 15)
plt.xlabel("Mean Height (inches)")
plt.ylabel("Frequency")

# Annotate plot
plt.annotate("n = 30", xy=(0.70,0.90), xycoords='axes fraction')
plt.annotate("mean = " + str(round(av, 2)), xy=(0.70,0.85), xycoords='axes fraction')
plt.annotate("std. error = " + str(round(std_er, 3)), xy=(0.70,0.80), xycoords='axes fraction')

# Show the plot
plt.show()

# Print the mean and standard error
print (stats.mean(dist))
print (stats.pstdev(dist))


