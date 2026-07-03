# compute derivatives of basic function & gradient
import sympy as sp 
import numpy as np

r = sp.Symbol('r')
t = sp.Symbol('t')

g = r**2 - t**3

deri_r = sp.diff(g,r)
deri_t = sp.diff(g,t)

 
print("Gradient of R: ", deri_r)
print("Gradient of T: ", deri_t)


# implement gradient descent for linear regression

# define the gd function
# theta - weight
def gradient_descent(X,y, theta, learning_rate, iterations):
    m = len(y)

    for _ in range(iterations):
        predictions = np.dot(X, theta)
        errors = predictions - y
        gradients = (1/m) * np.dot(X.T, errors)
        theta -= learning_rate * gradients
    return theta

# X - feature matrix, y - actual target vector, theta - initial weights, learning_rate - step size, iterations - number of iterations

X = np.array([[1,2],
              [1,3],
              [1,4]])

y = np.array([5,7,9])

theta = [0,0]

result = gradient_descent(X, y, theta, learning_rate=0.01, iterations=1000)
print("Final weights:", result)