n = int(input('How many numbers do you need in your list?! '))
l = []
for i in range(n):
    nn = int(input('Enter: '))
    l.append(nn)

l.reverse()
print(l)
