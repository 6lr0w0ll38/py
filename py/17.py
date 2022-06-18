from sympy import *

x = symbols ('x')

print((E ** x * tan(x)).series(x , 0 , 5))
