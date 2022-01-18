import math
a, b = float(input('1st side of triangle ')), float(input('2nd side of triangle '))
c = float(input('3rd side of triangle '))
p = (a + b + c) / 2
print('Area of triangle is', math.sqrt(p * (p - a) * (p - b) * (p - c)))
