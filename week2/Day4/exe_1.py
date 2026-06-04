# Ex-1: Clean a Dataset by Handling Missing value and renaming cloumns

import pandas as pd
import numpy as np

data = {
    "Name": ["Khali", "Miko", np.nan, "Josi"],
    "Age": [25, np.nan, 30, 45],
    "Score": [85, 90, np.nan, 88]
}

df = pd.DataFrame(data)

print('Original Df: \n', df)

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Score"] = df["Score"].interpolate()

df["Name"] = df["Name"].fillna("Alex", inplace=True)

print("Updated Dataset: \n", df)