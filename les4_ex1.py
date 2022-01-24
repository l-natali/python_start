x = int(input())
x = list(map(int, str(x)))
x1 = x[0]
x2 = x[1]
x3 = x[2]
x4 = x[3]
if x1 + x2 == x3 + x4:
    print('Happy ticket')
else:
    print('Not happy ticket')
