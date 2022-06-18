from sympy import *

x , n = symbols ('x n')

print (Sum ( n * x ** n , (n , 0 , oo ) ) . doit ())
