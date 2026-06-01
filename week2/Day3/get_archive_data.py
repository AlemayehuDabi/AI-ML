# https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data
# exe - load and explore a sample dataset
import requests
import pandas as pd
from io import StringIO

# loading the data - one time
response = requests.get('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')

response.raise_for_status()
data = pd.read_csv(StringIO(response.text), header=None)


df = pd.DataFrame(data)

# saving
saved_csv = df.to_csv("./fetched_csv.csv", index=False)