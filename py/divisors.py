#find divisors
# ##use package
# from sympy import *
# print (divisors(24))

##use loop
import math
def divisors(n):
    a = []
    for _ in range(1, math.isqrt(n) + 1):
        if n % _ == 0:
            a.append(_)
            a.append(n // _)
    return a

#drive code
print ('n:')
n = int(input())
print (divisors(n))

