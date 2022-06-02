import random

def check(x, b, e):
        if e < x or x < b:
            print ('false, reinput: ')
            x = int(input())
        else:
            return x
        return check(x, b, e)

print ('b, e:')
b, e = (int(input()) for _ in range(2))
print ('input number [' , b, ',', e, ']')
x = int(input())
x = check(x, b, e)
a = random.randrange(b, e)
flag = 0
while x != a:
    print ('your lost\n')
    if x < a:
        print ('your can input number biger:\n')
        b = x
        print ('input number [' , b, ',', e, ']')
    else:
        print ('your can input number smaller:\n')
        e = x
        print ('input number [' , b, ',', e, ']')
    x = int(input())
    x = check(x, b, e)
    flag += 1
    if flag == 5:
        print(a)
print ('your win')



