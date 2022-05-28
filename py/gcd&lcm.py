# ##Use package
# from sympy import *
# print (gcd(91, 287))

##Use loop
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# ##Use recursive
# gcd = lambda a, b: a if b == 0 else gcd(b, a % b)

#drive code
print('input a, b: ')
a, b = (int (input()) for _ in range(2))
lcm = a * b / gcd(a ,b)
print (gcd(a, b))
print (lcm)
