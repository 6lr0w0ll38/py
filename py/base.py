##base b in dec
#def
def base_to_value(a, b):
    n = 0 #n is dec
    p = 1
    for _ in reversed(a):
        n += _ * p
        p *= b
    return n

# #horner
# def base_to_value(a,b):
#     n = 0
#     for _ in a:
#         n = n * b + _
#     return n

#drive code
print ('base: ')
b = int(input())
print ('nb fm list:')
a = list(map(int, input().split()))
print (base_to_value(a, b))
