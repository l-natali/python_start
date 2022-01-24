x = int(input('The year is '))
if x % 400 == 0:
    print('It is leap-year')
elif x % 100 == 0:
    print('It is not leap-year')
elif x % 4 == 0:
    print('It is leap-year')
else:
    print('It is not leap-year')
