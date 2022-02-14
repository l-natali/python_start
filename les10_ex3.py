def rectangle(a, b):
    a1 = b * '*' + '\n'
    bn = '*' + (' ' * (b - 2)) + '*' + '\n'
    return a1 + (bn * (a - 2)) + a1


a, b = int(input('a = ')), int(input('b = '))
print(rectangle(a, b))
