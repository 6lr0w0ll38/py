#a, b and in a base
##sum |a| = |b|
def sum_in_base(a, b, base):
    l = len(a)
    s = []
    m = 0
    for _ in range(l - 1, -1, -1):
        s.append((a[_] + b[_] + m) % base)
        m = (a[_] + b[_] + m) // base
    s.append(m)
    return s

#drive code
print ('base:')
base = int(input())
print ('a:')
a = list(map(int, input().split()))
print ('b:')
b = list(map(int, input().split()))
print ('sum: ', list(reversed(sum_in_base(a, b, base))))

##mul
