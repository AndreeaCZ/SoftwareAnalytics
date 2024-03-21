import sqlite3
from scipy.stats import f_oneway


conn = sqlite3.connect('../db')

c = conn.cursor()

features = ['num_comments', 'perc_inte_neg_emo', 'perc_contrib_neg_emo', 'perc_neg_emotion', 'perc_pos_emotion']
features_string = ', '.join(features)

query = f'select {features_string} from filtered_data where contrib_first_emo != "" and inte_first_emo != ""'

c.execute(query + ' and same_country = 1')

same_country = {}
different_country = {}
data = c.fetchall()
for i in range(len(features)):
    same_country[features[i]] = [float(row[i]) for row in data if row[i] != '']

c.execute(query + ' and same_country = 0')
data = c.fetchall()
for i in range(len(features)):
    different_country[features[i]] = [float(row[i]) for row in data if row[i] != '']

c.close()
conn.close()

# do anova on each
for feature in features:
    f, p = f_oneway(same_country[feature], different_country[feature])
    print(f'f: {f}, p: {p} for {feature}')
