x = int(input('Print 6-digit number '))
x = list(map(int, str(x)))
y = x.copy()
y.reverse()
if x == y:
    print('Palindrom')
else:
    print('Not palindrom')
