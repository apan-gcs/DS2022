# numpy: Doing math on arrays (upgraded lists)

# A new library "numpy" (Numerical Python), commonly abbreviated as "np"
import numpy as np

# A regular Python list object. Same as list(range(1,6))
regularlist = [1, 2, 3, 4, 5]

# Converting the above list into an ndarray called x
x = np.asarray(regularlist)

# You can do math on ndarrays. Compare:
print(regularlist * 2)
print(x * 2)

# This one isn't even possibly with lists.
print(x + 0.5)

# ndarrays are also iterable, just like lists.
for i in x:
    print(i)

# [USEFUL!] Two functions for generating evenly-spaced numbers
# Use arange() for integers, linspace() for floating point numbers
print(np.arange(1, 6))          # Same as range(), but for ndarrays; [1,6)
print(np.linspace(0, 10, 11))   # start, end, num (number of points generated)

# You can also find functions like sin, cos, arctan, etc.
# https://numpy.org/doc/stable/reference/routines.math.html
# print(np.log(x))