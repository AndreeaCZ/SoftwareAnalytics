import sqlite3
from scipy.stats import f_oneway
import numpy as np

conn = sqlite3.connect('../db')
c = conn.cursor()

c.execute('select inte_country, perc_inte_neg_emo from filtered_data where inte_first_emo != "" and inte_first_emo is not null '
          'and (inte_country == "united states" or inte_country == "united kingdom" or inte_country == "japan")')

data = c.fetchall()

lists = {}
for x in data:
    if x[1] == '':
        continue
    if x[0] not in lists:
        lists[x[0]] = []
    lists[x[0]].append(float(x[1]))

# show average
for key in ['united states', 'united kingdom', 'japan']:
    print(f'{key} average neg_emotion: {np.mean(lists[key])}, len: {len(lists[key])}')


# do anova on each pair
def anova(key1, key2):
    f, p = f_oneway(lists[key1], lists[key2])
    print(f'f: {f}, p: {p} for {key1} and {key2}')

anova('united states', 'united kingdom')
anova('united states', 'japan')
anova('united kingdom', 'japan')