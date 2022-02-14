import random


def max_num(a):
    for i in a:
        amax = max(a)
        return amax


a = [random.randint(1, 100) for _ in range(15)]

print(a)
print(max_num(a))
