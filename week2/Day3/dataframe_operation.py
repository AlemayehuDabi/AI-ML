import pandas as pd

data = {"Name": ["Khali", "Miko", "Josi", "Eyosi", "Bebe"], "Age": [17,15, 13, 22, 23]}
df_data = pd.DataFrame(data)
# print(df_data)

# see the first 5 row
head = df_data.head()
# print(head)
# see the first 3 row - head(3)

# see the last 5 tail
tail = df_data.tail()
# to see the tast 3 use - tail(3)
# print(tail)

# summary info
# summary = df_data.info()
# print(summary)

# detailed info
detail = df_data.describe()
# print(detail)

# selecting and indexing
# selecting columns
col = df_data[["Name"]]
# print(col)

# filtering rows
fil_row = df_data[df_data["Age"] < 20]
# print(fil_row)

# selecting by position
select_row_first_index = df_data.iloc[0] # by row
# print(select_row_first_index)
select_col_first_index = df_data.iloc[:, 0] # by col
# print(select_col_first_index)
select_col_second_index = df_data.iloc[:, 1] # but if the index execed - python interpreter throws error saying out-of-bounds 
# print(select_col_second_index)

# selecting by level
select_level_name = df_data.loc[:,"Name"]
# print(select_level_name)