# #permutations
# ##use package
# import itertools
# print (list(itertools.permutations([1, 2, 3], 3)))

##use recursive
def permutations(a, n):
    b = a.copy()

#driver code
print ('input n: ')
n = int(input())
print ('input list a:')
a = list(map(int, input().split()))
permutations(a, n)
