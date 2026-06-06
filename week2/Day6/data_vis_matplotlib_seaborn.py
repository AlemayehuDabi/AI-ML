import matplotlib.pyplot as plt

# Basic Matplotlib synthax
x = ['Ana','Khali','Miko','Josi']
y= [10,17, 15, 14]

# plt.plot(x,y)
# plt.show()

# Line Plot
# plt.plot(x,y,label='Trend')
# plt.title("Line Plot")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.legend()
# # plt.show()

# Bar Chart
# plt.title('Students Age')
# plt.bar(x,y, color='blue')
# plt.show()

# Histogram
data = [1,2,2,3,3,4,4,4,5,5,5,6,6]
plt.hist(data, bins=4, color='blue', edgecolor='green')
plt.title('Histogram')
plt.show()