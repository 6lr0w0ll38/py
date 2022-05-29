#a, b and in a base
##sum
def sum_in_base(a, b, base):
    la = len(a) - 1
    lb = len(b) - 1
    s = []
    m = 0
    while la != -1 and lb != -1:
        s.append((a[la] + b[lb] + m) % base)
        m = (a[la] + b[lb] + m) // base
        la -= 1
        lb -= 1
    if la == -1:
        for _ in range(lb , -1, -1):
            s.append((b[_] + m) % base)
            m = (b[_] + m) // base
    else:
        for __ in range(la, -1, -1):
            s.append((a[__] + m) % base)
            m = (a[__] + m) // base
    s.append(m)
    return s

def check(x, base):
    if max(x) >= base:
        print ('false, reinput: ')
        x = list(map(int, input().split()))
    else:
        return x
    return check(x, base)

#drive code
print ('base:')
base = int(input())
print ('a:')
a = list(map(int, input().split()))
a = check(a, base)
print ('b:')
b = list(map(int, input().split()))
b = check(b, base)
print ('sum: ', list(reversed(sum_in_base(a, b, base))))

##mul
