#check prime
# ##use package
# from sympy import *
# print (isprime(3))

##use loop
import math
def isprime(n):
    for _ in range(2, math.isqrt(n) + 1):
        if n % _ == 0:
            print ('False')
            break
    else:
        print('True')

#driver code
print ('n:')
n = int(input())
isprime(n)
