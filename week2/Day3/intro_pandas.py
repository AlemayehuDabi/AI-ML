import pandas as pd

# series
ser = pd.Series([10,20,30], index=["a", "b", "v"])
# print("series: \n", ser)

# data-frame
data = {"Name": ["Khali", "Miko"], "Age": [17, 15]}
data_frame = pd.DataFrame(data)

# print(data_frame)

# saving data
data_frame.to_csv("./data_check.csv", index=False)
data_frame.to_excel("./data_check.xlsx", index=False)

# loading data
ldc = pd.read_csv('./data_check.csv')
# print(ldc)
lde = pd.read_excel('./data_check.xlsx')
# print(lde)
