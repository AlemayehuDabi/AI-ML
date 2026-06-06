import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

# Basic Matplotlib synthax
x = ['Ana','Khali','Miko','Josi']
y= [10,17, 15, 14]

# plt.plot(x,y)
# plt.show()

# Line Plot - visualize trends overtime
# plt.plot(x,y,label='Trend')
# plt.title("Line Plot")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.legend()
# # plt.show()

# Bar Chart - catagories data comparision
# plt.title('Students Age')
# plt.bar(x,y, color='blue')
# plt.show()

# Histogram - shows the distrbution of dataset
# data = [1,2,2,3,3,4,4,4,5,5,5,6,6]
# plt.hist(data, bins=4, color='blue', edgecolor='green')
# plt.title('Histogram')
# plt.show()

# scatter plot
# plt.scatter(x,y,color='Red') # it is used to visualize the r/ship b/n two cont variables 
# plt.title("Show the potenitial danger area")

# plt.show()


#  ---------------------- Seaborn ----------------------------
data = np.random.rand(5,5)
# heatmap
# sns.heatmap(data, cmap='coolwarm', annot=True)
# plt.title("Heat Map")
# plt.show()

df = pd.DataFrame(data)

# pairplot
sns.pairplot(df)
plt.show()