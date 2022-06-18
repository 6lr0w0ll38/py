# ##use package
# from sympy import *
# print (factorint(1176))

##use loop
def factorint(n):
    _ = 2
    dict = {}
    while n > 1:
        e = 0
        while n % _ == 0:
            n //= _
            e += 1
        if e:
            dict[_] = e
        _ += 1
    return dict

#driver code
print ('n:')
n = int(input())
print (factorint(n))
