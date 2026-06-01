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
summary = df_data.info()
# print(summary)

# detailed info
detail = df_data.describe()
print(detail)
