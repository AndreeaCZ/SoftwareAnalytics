import sqlite3
import pandas as pd
import statsmodels.api as sm

# Connect to the SQLite database
conn = sqlite3.connect('identifier.sqlite')

# Query the data from the database
query = "SELECT reponame, team_size, num_commits, num_comments, project_age, AVG(mergetime_minutes) AS avg_mergetime, COUNT(DISTINCT inte_country) AS num_countries FROM filtered_data GROUP BY reponame"
data = pd.read_sql_query(query, conn)

# Close the database connection
conn.close()

# Define the independent variable (number of countries) and dependent variable (average merge time)
X = sm.add_constant(data[['num_countries', 'team_size', 'num_commits', 'num_comments', 'project_age']])  # Independent variable (with constant term)
y = data['avg_mergetime']  # Dependent variable

# Fit the linear regression model
model = sm.OLS(y, X).fit()

# Print the summary of the regression results
print(model.summary())
