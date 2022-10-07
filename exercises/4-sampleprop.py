# Sampling Distribution for Sample Proportion

from matplotlib import pyplot as plt
import statistics as stats
import random
from pandas import read_csv

# Import data set and convert to a list
file_name  = "pets.csv"
data = read_csv(file_name, header = None)
data = data[0].values.tolist()


# Variables
samples = 1000   # Number of samples taken
n = 30           # Sample size

dist = []        # Sampling distribution of sample means
random.seed(1)


# Sampling with loops
# Only the sample proportion is recorded and added to dist
for i in range(samples):
    
    # Take a SRS of size n (with replacement; w/o is also okay)
    samp = random.choices(data, k=n)
    # samp = random.sample(data, k=n)
    

    # Calculate the sample proportion
    yesses = samp.count("yes")
    s_prop = yesses / n
    
    # Append to the distribution / dist
    dist.append(s_prop)


# Mean and Stdev (Standard Error) of Sampling Distribution
sd_mean = stats.mean(dist)
sd_error = stats.pstdev(dist)

print("Sampling Distribution Mean:", round(sd_mean, 4))
print("Sampling Distribution Std Error:", round(sd_error, 6))

# Mean of dataset
print("Population Mean:", data.count("yes") / len(data))

# Optional pyplot format editing
# plt.xkcd(0.8)
plt.style.use("ggplot")

# Plot a histogram ; bins and rwidth are optional
plt.hist(dist, bins = 20, rwidth = 0.9)

plt.title("Sampling Distribution of Pet Ownership", fontsize = 13)
plt.xlabel("Sample Proportion that Own a Pet")
plt.ylabel("Frequency")


plt.annotate("n = " + str(n), xy = (0.04, 0.92), xycoords = "axes fraction")
plt.annotate("Mean = " + str(round(sd_mean, 2)),
             xy = (0.04, 0.86), xycoords = "axes fraction")
plt.annotate("Std Err = " + str(round(sd_error, 3)),
             xy = (0.04, 0.80), xycoords = "axes fraction")

plt.show()
