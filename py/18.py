# b , c = 4 , 1
# n = 10
# for i in range (2 , n +1) :
#     a = 3* b - 2* c + i
#     c , b = b , a
#     print (i , a)

from sympy import *
n = symbols ('n')
a = symbols ('a', cls = Function)
print(rsolve ( -a(n) + 3 * a(n -1) - 2 * a(n -2) + n, a(n), {a(0) : 1, a(1) : 4}) . simplify ())
