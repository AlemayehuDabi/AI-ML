import matplotlib.pyplot as plt

# Basic Matplotlib synthax
x = [1,2,3,4,5]
y= [10,20,35,60,75]

plt.plot(x,y)
plt.show()

# Line Plot
plt.plot(x,y,label='Trend')
plt.title("Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()