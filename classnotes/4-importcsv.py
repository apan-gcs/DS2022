
# We use a function from pandas to import csv files.
from pandas import read_csv

# Paste the file path to your csv here.
# The file must be in your working directory (usually same as your program)
filename = "pets.csv"

# Importing the file as a pandas.DataFrame
# In this case, single-column and no header
data = read_csv(filename, header = None)

# Then converting in to a regular list
data = data[0].values.tolist()

print(data)

