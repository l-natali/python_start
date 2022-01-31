import random
a = []
n = int(input('Input length of list '))
j = -1
for i in range(n):
    a.append(random.randint(1, 100))
print(a)
for i in a:
    if n == -j // 2:
        break
    else:
        a.insert(i, a[j])
        j -= 2
del a[0:n]
print(a)
