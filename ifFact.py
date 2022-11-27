import math


f = []
for i in range(100):
    ff = math.factorial(i)
    f.append(ff)

n = int(input('is this number a factorial one or not?!'))
if n in f:
    print('Yes it is!')
else:
    print("Nah it's not")