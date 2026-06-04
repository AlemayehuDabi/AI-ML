# concat, merge, join
import pandas as pd
# import numpy as np

df1 = pd.DataFrame({
    "id": [1, 2, 3],
    "name": ["Alice", "Bob", "Cara"],
    "age": [25, 30, 38]
})

df2 = pd.DataFrame({
    "id": [3, 4],
    "name": ["Cara", "Dan"],
    "age": [28, 35]
})

# concat
# row
df_row_concat = pd.concat([df1,df2], ignore_index=True)
# print(df_row_concat)

# col
df_col_concat = pd.concat([df1, df2], axis=1)
# print(df_col_concat)


# merging
# inner
df_merge = df1.merge(df2, how='inner', on=['id', 'name'])
# print(df_merge)

# left
df_left_merge = df1.merge(df2, how='left', on=['age'])
# print(df_left_merge)

# right
df_right_merge = df1.merge(df2, how='right', on=['age'])
# print(df_right_merge)

# outer
df_outer_merge = df1.merge(df2, how='outer', on=['age'])
# print(df_outer_merge)

# joning
# - this under the hood uses the merge

# new data set
df_temp = pd.DataFrame({
    "STATION": ["S1", "S2", "S3"],
    "TEMP": [15, 20, 22]
}).set_index("STATION")

df_precip = pd.DataFrame({
    "STATION": ["S1", "S2", "S3", "S4"],
    "PRECIP": [10, 12, 8, 15]
})

# Join on STATION column to df_temp's index
result = df_precip.join(df_temp, on="STATION", how="left")
print(result)

# and this is just like the merge same for the how parameter