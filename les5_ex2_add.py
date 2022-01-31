a = int(input('a='))
i = 0
if a % 2 == 0:
    print('Error')
else:
    for j in range(a, 0, -2):
        print(' ' * i + '*' * j)
        i += 1
    i -= 2
    for j in range(3, a + 1, 2):
        print(' ' * i + '*' * j)
        i -= 1
