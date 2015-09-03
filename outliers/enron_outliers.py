#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
import pandas as pd

### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
data_dict.pop('TOTAL', 0)
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

### Encore des Outliers
mod_data = []
for k, v in data_dict.iteritems():
    row = v
    row['name'] = k
    mod_data.append(row)
df = pd.DataFrame(mod_data)

remove_nan_Df = df[df.salary != 'NaN']
over1m_salary_df = remove_nan_Df[remove_nan_Df.salary > 1e6]
over1m_salary_over_5m_bonus_df = over1m_salary_df[over1m_salary_df.bonus > 5e6]
print over1m_salary_over_5m_bonus_df['name']