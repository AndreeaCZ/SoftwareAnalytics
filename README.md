## Software Analytics project by Group 4
### Matej Kucera & Andreea Zelko

## Project description
The topic of this project is:
```Increase global collaboration — impact on review speed in industry```

We perform a statistical analysis on a dataset of pull requests from GitHub. The dataset is obtained from [https://zenodo.org/records/3922907](). 
We are grateful to Zhang et al., the authors of <b>On the Shoulders of Giants: A New Dataset for Pull-based
Development Research</b> for providing this dataset.

## Research questions
1. Does the time to merge a pull request change depending on whether the contributor and integrator are from the same country?
2. Does the average time to merge a pull request for a repository depend on the number of countries collaborating?
3. Does the percentage of negative comments on a pull request depend on whether the integrator and contributor are from the same country?
4. Are there certain countries which have a higher percentage of negative comments on pull requests when in the role of an integrator?

## Data
The dataset is quite large (~2GB) and contains a lot of pull requests. We have filtered the dataset using the SQL query which can be found in ```filtered_data.sql```. 
The resulting dataset can be found in ```filtered_data.csv```. For questions regarding emotions, we had to exclude PRs from this dataset which don't contain emotion analysis data. 
The emotion analysis dataset and the SQL command used to obtain it can be found in ```emotion_data.sql``` and ```emotion_data.csv```.

## Analysis
The Python code we used to analyze the data can be found in the files ```rq1.py```, ```rq2.py```, ```rq3.py``` and ```rq4.py```. Additional code used to visualize the data is in ```histogram.py```.

## Methodology

We used linear regression for RQ1 and RQ2 in order to find whether there is a significant relationship between the variables. 
We used several control variables in our analysis as can be seen in the corresponding source code files.

For RQ3 and RQ4, we used the ANOVA test to determine whether there is a significant difference between the groups.

## Results
The results of our analysis are presented in a blogpost which can be found at the following link: [google.com]().