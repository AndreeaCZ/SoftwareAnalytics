import sqlite3
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import f_oneway


conn = sqlite3.connect('db')

c = conn.cursor()

# just does anova on whatever you select
# c.execute('select perc_neg_emotion, same_country from filtered_data')
#
# same_country = []
# different_country = []
# for row in c:
#     if row[0] == '':
#         continue
#     if row[1] == 1:
#         same_country.append(float(row[0]))
#     else:
#         different_country.append(float(row[0]))
#
# c.close()
#
# f, p = f_oneway(same_country, different_country)
# print(f'f: {f}, p: {p}')


# RQ2
c.execute('SELECT fd.mergetime_minutes, nc.num_countries FROM filtered_data fd JOIN (SELECT reponame, COUNT(DISTINCT '
          'contrib_country)'
          'AS num_countries FROM new_pullreq GROUP BY reponame) nc ON fd.reponame = nc.reponame;')
data = c.fetchall()
print(len(data))

c.close()

# correlation
boxplot_data = []
for i in range(1, 45):
    arr = [mergetime for mergetime, num_countries in data if num_countries == i]
    if len(arr) > 0:
        boxplot_data.append(arr)

print(f'boxplot_data: {boxplot_data}')
plt.boxplot(boxplot_data)
plt.show()

f, p = f_oneway(*boxplot_data)

print(f'f: {f}, p: {p}')

conn.close()