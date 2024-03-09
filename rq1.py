import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
import statsmodels.api as sm

# Connect to the SQLite database
conn = sqlite3.connect('identifier.sqlite')

# Query the data from the 'filtered_data' table into a pandas DataFrame
query = "SELECT * FROM filtered_data"
data = pd.read_sql_query(query, conn)

# Close the database connection
conn.close()


# Define the independent variables (features) and dependent variable
X = data[['same_country', 'team_size', 'num_commits', 'num_comments', 'project_age']]  # Independent variables
Y = data['mergetime_minutes']  # Dependent variable

# # Get the data types of each column
# all_columns = X.columns
# data_types = X.dtypes
#
# # Find columns with object or string data types
# categorical_features = data_types[data_types == 'object'].index.tolist()
# # Identify numerical features by excluding the categorical features
# numerical_features = [col for col in all_columns if col not in categorical_features]
#
#
# # Perform one-hot encoding for categorical features
# encoder = OneHotEncoder(drop='first')
# encoder.fit(X[categorical_features])
# encoded_categorical_features = encoder.transform(X[categorical_features])
# encoded_categorical_feature_names = encoder.get_feature_names_out(categorical_features)
#
# # Combine encoded categorical features and numerical features
# X_encoded = pd.concat([pd.DataFrame(encoded_categorical_features, columns=encoded_categorical_feature_names), X[numerical_features]], axis=1)
#

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Train the Multiple Linear Regression model
# model = LinearRegression()
# model.fit(X_train, y_train)
#
# # Print the coefficients
# print('Intercept:', model.intercept_)
# print('Coefficients:', model.coef_)
#
# # Evaluate the model
# train_score = model.score(X_train, y_train)
# test_score = model.score(X_test, y_test)
# print('Train R^2 Score:', train_score)
# print('Test R^2 Score:', test_score)

X_train = sm.add_constant(X_train)
X_test = sm.add_constant(X_test)

# Train the Multiple Linear Regression model
model = sm.OLS(y_train, X_train)
result = model.fit()

# Print the summary which includes coefficients
print(result.summary())

# Evaluate the model
train_score = result.rsquared
test_score = result.rsquared_adj
print('Train R^2 Score:', train_score)
print('Test R^2 Score:', test_score)
