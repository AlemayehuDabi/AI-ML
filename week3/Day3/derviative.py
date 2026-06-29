import sympy as sp

x = sp.Symbol('x')
f = x**2

derviative = sp.diff(f, x)
print("Derviative: \n", derviative)

# partial derivatives
r = sp.Symbol('r')
t = sp.Symbol('t')

g = r**3 + t*2

par_deri_r = sp.diff(g,r)
par_deri_t = sp.diff(g,t)


print("Partial Derviative of R: ", par_deri_r)
print("Partial Derviative of T: ", par_deri_t)