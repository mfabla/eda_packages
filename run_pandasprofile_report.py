# exploring EDA with pandas profiling package using titanic training data
# need to do a !pip install of 'pandas-profiling' to run this script

import pandas as pd
import pandas_profiling as pp

# load titanic data
df = pd.read_csv("titanic_train.csv")
df.head()

# run the eda one-line code to run the eda report and export as html
report = pp.ProfileReport(df) # to display report
report.to_file('profile_report.html')

# that's it!!