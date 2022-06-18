print ('input number of row: ')
nor = int(input())
for i in range (nor):
    n = 0
    print ('\n')
    while n < 2 * i + 1:
        print (i + 1, ' ', end = '')
        n += 1
