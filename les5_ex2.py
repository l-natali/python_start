n = int(input('n='))
i = 1
f = 1
if 4 < n < 16:
    while i <= n:
        f = i * f
        i += 1
    print(f)
else:
    print('Error')
