"""
Ms. Pan's comments"

- The original code doesn't run due to the original formatting of the header!
  Always check to make sure your code runs before submitting.
- Capitalize your comments, don't put spaces after a function name
  (annotate!), make a linebreak after `else:`.
- You can try enabling Spyder auto-formatting, although it will sometimes do
  things you don't want it to do. But it can help.
- You ended up printing mean and stdev twice. Also, it should be "pstdev".
- See the 'EDIT' comments throughout.
"""

'''
Gaspar Salcedo-Galli
10/7/22
Ms. Pan
Intensive Data Science II
Q1 Miniproject'''

# EDIT: deleted this import statement.
from matplotlib import pyplot as plt
import random
import statistics
from pandas import read_csv

# random seed
random.seed(1)

# import dataset
data = read_csv("pets.csv", header=None)
data = data[0].values.tolist()


# define variables
samples = 1000  # number of samples
n = 30          # sample size
bigsamp = []


# simulate list of proportions of random samples
# EDIT: Break this up with comments, it's hard to figure out what is going on.
# If I hadn't done this with you, it'd take me a few minutes.
for i in range(samples):
    samp = []
    
    for i in range(n):
        if random.choice(data) == "yes":
            samp.append(1)
        else:
            samp.append(0)
            
    mean = sum(samp) / n
    bigsamp.append(mean)


# calculate mean and stdev
tmean = round(sum(bigsamp) / 1000, 4)
print(tmean)
stdev = round((statistics.pstdev(bigsamp)), 4)
print(stdev)


# plot graph
plt.hist(bigsamp)  # EDIT: Put this first

plt.title("Sampling Distribution")
plt.xlabel("Distribution of Sample That is a Pet Owner")
plt.ylabel("Frequency")  # EDIT: Why shorten this to 'freq'?

# EDIT: deleted the space between -> annotate (f"text").
plt.annotate(f"samples={samples}", xy=(0.03, 0.9), xycoords='axes fraction')
plt.annotate(f"n={n}", xy=(0.03, 0.85), xycoords='axes fraction')
plt.annotate(f"mean={tmean}", xy=(0.03, 0.80), xycoords='axes fraction')
plt.annotate(f"stdev={stdev}", xy=(0.03, 0.75), xycoords='axes fraction')

plt.show()

# EDIT: deleted the final print for mean and stdev