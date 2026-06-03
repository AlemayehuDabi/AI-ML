# concat, merge, join
import pandas as pd
import numpy as np

read_csv = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

df = pd.DataFrame({"Employee": ["Amina", "James", "Priya", "Chen", "Maria", "Omar"],
    "Age": [29, np.nan, 34, 41, np.nan, 27],
    "City": ["London", "Birmingham", np.nan, "Manchester", "Leeds", np.nan],
    "Salary": [52000, 48000, np.nan, 61000, 54000, np.nan],
    "Join_Date": ["2022-03-14", "2021-11-01", "2023-06-20", np.nan, "2020-09-05", "2024-01-18"]})

# row df
# print("Row Df: \n", df)

# droping row w/ nan value
row_without_nan = df.dropna()
# print("Drop row w/ nan value: \n", row_without_nan)

# droping col w/ nan value
col_without_nan = df.dropna(axis=1)
# print("Drop col w/ nan value: \n", col_without_nan)


# filling missing values
# specific value
df["Age"] = df["Age"].fillna(0)
# print("df after filling it w/ specific value: \n", df)

# forward fill
df["City"] = df["City"].ffill()
# print("df after ffill: \n", df)

# backward fill
df["Join_Date"] = df["Join_Date"].bfill()
# print("df after bfill: \n", df)

# interpoliation
df["Salary"] = df["Salary"].interpolate()
# print("after interpolated: \n", df)

# renaming columns
df.rename(columns={"Salary": "Payment"}, inplace=True) # we use inplace to make the change on the existing df
# print("renamed: \n", df)

# Data Type Casting
df["Payment"] = df["Payment"].astype('int')
# print("Changing the Data types: \n", df)