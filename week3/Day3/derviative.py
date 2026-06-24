import sumpy as sp

x = sp.symbol('x')
f = x**2

derviative = sp.diff(f, x)
print("Derviative: \n", derviative)