x, y = int(input('x=')), int(input('y='))
x_list = range(-4, 5)
y_list = range(-4, 5)
if x in x_list and y in y_list:
    print('Point is inside circle')
else:
    print('Point does not inside circle')
