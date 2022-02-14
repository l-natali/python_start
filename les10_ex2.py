def stroka(a, b, c):
    summa = a + b
    summa = str(summa)
    concat = summa + c
    return concat


a, b = int(input('a = ')), int(input('b = '))
c = input('c - ')
print(stroka(a, b, c))
