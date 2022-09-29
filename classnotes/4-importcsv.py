
# We use a function from pandas to import csv files.
from pandas import read_csv

# Paste the file path to your csv here.
# The .csv file must be in the same folder as your program.
filename = "pets.csv"


# Importing the file as a DataFrame
# Then converting in to a regular list
data = read_csv(filename, header=None)
data = data[0].values.tolist()

print(data)

