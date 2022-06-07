#n = value dec
#b = base
#a = value base

# ##base b in dec
# #use def
# def base_to_value(a, b):
#     n = 0 #n is dec
#     p = 1
#     for _ in reversed(a):
#         n += _ * p
#         p *= b
#     return n
#
# # # #use horner
# # # def base_to_value(a,b):
# # #     n = 0
# # #     for _ in a:
# # #         n = n * b + _
# # #     return n
#
# #driver code
# print ('base: ')
# b = int(input())
# print ('nb fm list:')
# a = list(map(int, input().split()))
# print (base_to_value(a, b))

##dec in base b use horner
def value_in_base(n, b):
    a = []
    while n != 0:
        a.append(n % b)
        n //= b
    return a

#driver code
print ('value in dec:')
n = int(input())
print('base:')
b = int(input())
print (list(reversed(value_in_base(n, b))))
