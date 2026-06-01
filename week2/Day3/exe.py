import pandas as pd

# loading the data from saved file - instead of fetching everytime from the internet
loaded_data = pd.read_csv('./fetched_csv.csv')

# explore
# viewing the first 3 row
first_three_row = loaded_data.head(3)
# print(first_three_row)

# viewing the last 3 row
last_three_row= loaded_data.tail(3)
# print(last_three_row)

# summary info
# summ_info = loaded_data.info()

# detail stat
des_data = loaded_data.describe()
# print(des_data)

# Selecting and indexing
# selecting col
first_col = loaded_data[["0"]]
# print(first_col)

# filtering rows
filter_first_row = loaded_data[loaded_data['1'] > 2.2]
# print(filter_first_row)

# selecting by position
sel_row_pos = loaded_data.iloc[0]
# print(sel_row_pos)

# selecting by label
sel_col_pos = loaded_data.iloc[:, 0]
# print(sel_col_pos)

sel_label = loaded_data.loc[0]
# print(sel_label)



# using this dataset
# https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

print(df)

# explore
# viewing the first 3 row
first_three_row = df.head(3)
# print(first_three_row)

# viewing the last 3 row
last_three_row= df.tail(3)
# print(last_three_row)

# summary info
# summ_info = df.info()

# detail stat
des_data = df.describe()
# print(des_data)

# Selecting and indexing
# selecting col
first_col = df[["sepal_length"]]
# print(first_col)

# filtering rows
filter_first_row = df[df['sepal_width'] > 2.2]
# print(filter_first_row)

# selecting by position
sel_row_pos = df.iloc[0]
# print(sel_row_pos)

# selecting by label
sel_col_pos = df.iloc[:, 2]
# print(sel_col_pos)

sel_label = df.loc[:, "sepal_length"]
# print(sel_label)
