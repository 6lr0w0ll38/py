#abc = a^3 + b^3 + c^3

def exp3(t):
    t = t * t * t
    return t

#driver code
t = 101
while (exp3(t // 100) + exp3((t % 100) // 10) + exp3((t % 100) % 10) != t):
    t += 2
print (t)
