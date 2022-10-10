"""
Ms. Pan's comments:

- Deleted the import comment, but the other ones are concise and to the point.
  Maybe even a little too much, but it's fine.
- Better title than "Pet Sample"
- Edited formatting for annotations (e.g. moved down, added spaces).
- However, for plot annotations, the code should really insert
  the calculated value rather than a pre-determined value.
  (e.g. if I change the seed, the mean/stdev would be wrong.)
"""

# Robert Rendine Monday Oct-2-2022

from pandas import read_csv 
import matplotlib.pyplot as plt
from random import sample, seed
from statistics import pstdev

seed(1) # Random Seed

# CSV Reading
data = read_csv('pets.csv', header=None)
data = data[0].values.tolist()

# Variables
n = 30
dist = []

# Sampling
for i in range(0, 1000):
    sampledata = sample(data,k=n)
    yes = sampledata.count("yes")
    no = sampledata.count("no")
    dist.append(yes/n)

# Plot
plt.hist(dist, color = 'r', rwidth= .9)
plt.ylabel("Count")
plt.xlabel("Proportion")
plt.title("Sampling Distribution of Pet Owners")
plt.style.use("dark_background")

plt.annotate("n = 30", xy=(0.05, 0.92), xycoords='axes fraction')
plt.annotate("Mean: 0.32", xy=(0.05, 0.87), xycoords='axes fraction')
plt.annotate("StDev: 0.081", xy=(0.05, 0.82), xycoords='axes fraction')
plt.show()

# Mean and Standard Deviation
print("The Mean is:", (sum(dist)/1000))
print("The Standard Deviation is:", (pstdev(dist)))