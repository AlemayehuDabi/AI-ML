# integral
import sympy as sp

x = sp.symbols('x')
f = x**2

definite_integral = sp.integrate(f, (x, 0, 1))
indefinite_integral = sp.integrate(f, x)

print("Definite integral of x^2 from 0 to 1:", definite_integral)
print("Indefinite integral of x^2:", indefinite_integral)