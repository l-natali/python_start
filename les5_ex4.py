a, b = int(input('a=')), int(input('b='))
i = 0
print(b * '*')
while i < a - 2:
    print('*', ' ' * (b - 2), '*', sep='')
    i += 1
    print(end='')
print(b * '*')
