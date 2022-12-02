n = int(input('How many numbers do you need in your list?! '))
l = []
for i in range(n):
    nn = int(input('Enter: '))
    l.append(nn)

f = 0
r = len(l) - 1
while f < r:
    temp = l[f]
    l[f] = l[r]
    l[r] = temp
    f += 1
    r -= 1
#l.reverse()
print(l)
