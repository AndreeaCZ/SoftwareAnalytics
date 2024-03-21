import matplotlib.pyplot as plt
import pandas as pd
import sqlite3

conn = sqlite3.connect('db')

c = conn.cursor()

c.execute('select contrib_country from filtered_data')

data = c.fetchall()

# Convert data to a pandas Series
series = pd.Series(data)

# Set the minimum count threshold
min_occurrences = 20

# Filter categories with counts less than min_occurrences
counts = series.value_counts()
filtered_series = series[series.isin(counts[counts >= min_occurrences].index)]

# Plot histogram
plt.hist(filtered_series, bins=len(filtered_series.unique()))
plt.xlabel('Categories')
plt.ylabel('Frequency')
plt.title('Histogram of Categorical Variables (Excluding <10 Occurrences)')
plt.show()