
# Plot heights.csv and a normal distribution

from matplotlib import pyplot as plt
import numpy as np
import scipy.stats as stats
import pandas as pd

# WHat
data = pd.read_csv("heights.csv", header=None)

mean = data[0].mean()
stdev = data[0].std()

print(mean, stdev)

#what is this
x = np.linspace(50, 70, 100)
normal = stats.norm.pdf(x, loc=mean, scale=stdev)

plt.hist(data, density=True, bins=20)

plt.plot(x, normal)

plt.show()
