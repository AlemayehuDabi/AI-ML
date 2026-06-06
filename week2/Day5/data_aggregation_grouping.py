import pandas as pd
import numpy as np


data = {
    'Region': ['East', 'East', 'West', 'West', 'North', 'North', 'South', 'South'],
    'Product': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
    'Sales': [150, 200, 300, 250, 180, 220, 270, 310],
    'Quantity': [10, 15, 20, 25, 12, 18, 22, 28]
}

df = pd.DataFrame(data)

# group by two cols
grouped = df.groupby(['Region', 'Product'])

grouped_sum = grouped.sum()
# print('Grouped Sum: \n', grouped_sum)

grouped_mean = grouped.mean()
# print('Grouped Mean: \n', grouped_mean)


# group by one col - and operate agg on specific col
group_one_col = df.groupby('Region')


do_sum_on_sales = group_one_col['Sales'].sum()
# print('Do Sum on Sales Col: \n', do_sum_on_sales)

# use agg method
do_agg_on_group = group_one_col.agg({
    'Sales': ['mean', 'sum'],
    'Quantity': ['mean', 'sum']
})

# print('Using Agg funtion: \n', do_agg_on_group)

# count method on grouped data using two cols
do_count = grouped.count()
# print("Do Count: \n", do_count)

do_count_one_col_group = group_one_col.count()
# print("Do Count One Col: \n ", do_count_one_col_group)

# min
do_min = group_one_col.min()
# print("Do Min: \n", do_min)

# max
do_max = group_one_col.max()
# print("Do Max: \n", do_max)