# Ex1: Calculate the integral of simple functions using sympy
import sympy as sp

X = sp.symbols('X')

func = X**2 + 3*X + 5

definite_integral = sp.integrate(func, (X, 0,6))
indefinite_integral = sp.integrate(func)

print("Definite Integral: ", definite_integral)
print("Indefinite Integral: ", indefinite_integral)
