# We use a function from pandas to import Excel (.xlsx) files.
from pandas import read_excel

# Paste the file path to your Excel sheet here.
# The file must be in your working directory (usually same as your program)

# This particular file has two columns: "Time" and "Population"
filename = "5-population.xlsx"

# Importing the file as a pandas.DataFrame ('df')
df = read_excel(filename)

print(df.head())  # Prints first 5 rows of the data

# Access a column with square brackets and the column name.
# Each of these columns functions similarly to a list / ndarray.

years = df['Year']
pop = df['Population']

print(years)
print(pop)

# Optional: Convert population into billions
pop = df['Population'] / (10 ** 9)


# Try plotting Population vs. Year
import matplotlib.pyplot as plt

plt.plot(years, pop)

plt.title("World Population")
plt.xlabel("Year")
#plt.ylabel("Population")
plt.ylabel("Population (in billions)")

plt.xlim(1800, 2022)
plt.xticks(range(1800, 2021, 20), rotation = 50)

#plt.show()
