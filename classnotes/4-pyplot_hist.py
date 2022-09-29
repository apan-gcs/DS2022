# Class notes on basic pyplot and histograms
# See: https://matplotlib.org/stable/tutorials/introductory/pyplot.html

# Import the pyplot module (for plotting)
from matplotlib import pyplot as plt
import random

# Set up x and y coordinates as lists
x = [1, 2, 3,  4,  5]
y = [1, 4, 9, 16, 25]

# Plot y vs x as a scatterplot
# plt.scatter(x, y, marker='^', color='green')


# Exercise: Roll 3 dice, sum the rolls (simulate 100 times)

rolls = []

for i in range(100):
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    roll3 = random.randint(1,6)
    rolls.append(roll1 + roll2 + roll3)

# Setting up bins for histogram
# These bins make sure the actual rolls are centered in each interval
bins = [2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5,
        12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5]

# Make histogram
plt.hist(rolls, bins=bins)

# Edit title and axes
plt.title("My First Python Plot",  fontsize = 15)
plt.xlabel("Sum of 3 Dice Rolls")
plt.ylabel("Frequency")

# Custom x-axis tick marks
ticks = list(range(3,19))
plt.xticks(ticks)

# Annotate using 'axes fraction' - coordinates relative to plot area
plt.annotate("n=100", xy=(0.05, 0.90), xycoords='axes fraction')

# Show the plot (always necessary; like "print")
plt.show()
