import copy
import random
a = []
b = []
for i in range(4):
    a.append(random.randint(1, 100))
print(a)
b = copy.copy(a)
for i in a:
    b.append(i * 2)
print(b)
