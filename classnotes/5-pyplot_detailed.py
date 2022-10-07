# Class notes on pyplot graphs (specifically, scatterplot)
# See: https://matplotlib.org/stable/tutorials/introductory/pyplot.html

# PART 0) Importing
# Import the pyplot module (for plotting)
from matplotlib import pyplot as plt
import numpy as np


# PART 1) Setting up x and y data
# Set up x coordinates using linspace (arange is also ok)
x = np.linspace(0, 10, 11)   # [11 evenly-spaced points on [0,10]

# Three random mathematical functions
y1 = 3 * x                   # y = 3x
y2 = 0.5 * (x ** 2)          # y = 1/2 x^2
y3 = 2 * np.sin(x) + 10      # y = 2sin(x) + 10



# PART 1.5) Plot design (OPTIONAL)
# Use preset style sheets / "xkcd" style (they sort of conflict)
# plt.style.use("seaborn-darkgrid")
# plt.xkcd(0.5, 100, 4)


# PART 2) Plotting data
# Plot y vs x (see keywords in doc below)
# Other types of graphs include: bar, scatter, hist, pie, contour
# Doc: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
# Colors: https://matplotlib.org/stable/gallery/color/named_colors.html

plt.plot(x, y1, marker='^', color='green', markerfacecolor = "lime",
         linestyle = 'dashed', label = "3x")

plt.plot(x, y2, marker='x', color='royalblue', markersize = 10,
         label = "\u00BD x\u00B2")   # \uxxxx are unicode characters

plt.plot(x, y3, marker='o', color='#DD571C', linewidth = 4, alpha = 0.5,
         label = "2sin(x) + 10")



# PART 3) Editing plot components
# Set title and axes
plt.title("Mathematical Functions",  fontsize = 15)
plt.xlabel("x value", fontsize = 12)
plt.ylabel("y value", fontsize = 12)

# Set custom axis limits and ticks
plt.xlim(0, 10)
plt.ylim(0, 55)
plt.xticks(np.arange(0, 11, 1))



# PART 4) Add additional components on plot
# Legend uses labels from Part 2; keywords are optional
plt.legend()
#plt.legend(loc = "upper left", fontsize = 11,
#           frameon = 1, facecolor = "white", framealpha = 0.8)

# Annotatations: https://matplotlib.org/stable/tutorials/text/annotations.html
plt.annotate("Annotation", xy=(0.05, 0.65), xycoords='axes fraction')
plt.annotate("Crossover", xy=(6, 20), horizontalalignment = "right")



# PART 5) Show the plot (always necessary; like "print")
# Also, check Spyder's Preferences > iPython Console > Graphics for options
# You can adjust resolution, dimensions, and inline vs. popup (automatic)
plt.show()

