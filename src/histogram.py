import sqlite3
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pycountry


conn = sqlite3.connect('../db')

c = conn.cursor()

# change to contrib_country for the other histogram
c.execute('select inte_country from filtered_data')

data = c.fetchall()

data = [x[0] for x in data]

counts = {}
for x in data:
    if x not in counts:
        counts[x] = 1
    else:
        counts[x] += 1

counts_filtered = {}
for key in counts:
    if counts[key] > 20:
        counts_filtered[key] = counts[key]

plt.bar(counts_filtered.keys(), counts_filtered.values(), color='blue')
# plt.xticks(rotation='vertical')

plt.title('Histogram of Integrator Country')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels
# disable x-axis ticks
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=True)
plt.subplots_adjust(bottom=0.2)
plt.savefig('inte_histogram.png')

c.close()
conn.close()

