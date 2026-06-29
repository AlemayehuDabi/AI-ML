import sympy as sp

x = sp.Symbol('x')
f = x**2

derviative = sp.diff(f, x)
print("Derviative: \n", derviative)