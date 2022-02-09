import random
x = []
y = []
while len(x) < 10:
    a = random.randint(1, 100)
    if a % 3 == 0:
        x.append(a)
print(x)
while len(y) < 10:
    a = random.randint(1, 100)
    if a % 5 == 0:
        y.append(a)
print(y)
a, b = set(x), set(y)
print(a | b)
