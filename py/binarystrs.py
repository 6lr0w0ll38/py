#init binary strings with a lenght
def binary_strs(n):
    if n == 1:
        return ['0', '1']
    a = []
    for _ in binary_strs(n - 1):
        a.append('0' + _)
    for _ in binary_strs(n - 1):
        a.append('1' + _)
    return a

#driver code
print ('input lenght: ')
n = int(input())
print (binary_strs(n))
