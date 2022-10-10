"""
Ms. Pan's comments: Good overall, as usual. Edited a few parts, such as:
- Deleted importing comment; importing is normal.
- Changed comment format for the samples / n. Short comments can be nice
  on the side rather than at the top.
- x-label is more accurate as mean or average height, or sample mean of heights.
- Edited annotations. Split up the long ones into two lines, also
  shortened to "std. error" since it was close to the edge of the plot.
  It could also be fine on the left side.
- Optional, but the statistics module could do mean and pstdev for you.

"""


"""
Emma Gottfrid
September 29, 2022

Mini Project 1:
    Simulates the sampling distribution and generates a plot
"""

from pandas import read_csv
import matplotlib.pyplot as plt
import random
import math

# Importing heights data
filename = "heights.csv"
data = read_csv(filename, header = None)
data = data[0].values.tolist()

# In order to keep the results consistent
random.seed(1)

samples = 1000   # Number of samples
n = 30           # Sample size


# Collecting the samples for the histogram
dist = []

for i in range(samples):
    heights = random.sample(data, n)
    dist.append(sum(heights) / n)

    
# Finding the mean and Standard Error
mean = sum(dist) / samples
stderr = math.sqrt(sum([(x - mean)**2 for x in dist]) / samples)


# Plotting the histogram
plt.hist(dist, bins = 20, rwidth=0.93, color = "green")

# Labeling the title and axes of the histogram
plt.title("Sampling Distribution of Heights of 12-13 Year Olds", fontsize=15)
plt.xlabel("Mean Height (inches)", fontsize=12)
plt.ylabel("Frequency", fontsize=12)

# Annotations for n, the mean, and the standard error
plt.annotate(f"n={n}", xy=(0.68,0.93), xycoords='axes fraction', fontsize=11)
plt.annotate(f"mean = {str(round(mean,3))}", xy=(0.68,0.87),
             xycoords ='axes fraction', fontsize=11)
plt.annotate(f"std. error = {str(round(stderr,3))}", xy=(0.68,0.81),
             xycoords='axes fraction', fontsize=11)


# Printing the histogram, mean, and standard error
plt.show()
print(mean)
print(stderr)
