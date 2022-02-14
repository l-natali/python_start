import random


def search(s, el):
    if el in s:
        n = s.index(el)
    else:
        n = -1
    return n


s = [random.randint(1, 10) for _ in range(10)]
el = int(input('Input element - '))
print(s)
print(search(s, el))

