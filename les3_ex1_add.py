x = int(input('Print flat number '))
if 1 <= x <= 36:
    entrance = 1
    if x % 4 == 0:
        floor = x // 4
        print('Entrance is', entrance, 'Floor is', floor)
    else:
        floor = (x // 4) + 1
        print('Entrance is', entrance, 'Floor is', floor)
elif 37 <= x <= 72:
    entrance = 2
    if x % 4 == 0:
        floor = (x // 4) - 9
        print('Entrance is', entrance, 'Floor is', floor)
    else:
        floor = ((x // 4) + 1) - 9
        print('Entrance is', entrance, 'Floor is', floor)
elif 73 <= x <= 108:
    entrance = 3
    if x % 4 == 0:
        floor = (x // 4) - 18
        print('Entrance is', entrance, 'Floor is', floor)
    else:
        floor = ((x // 4) + 1) - 18
        print('Entrance is', entrance, 'Floor is', floor)
elif 109 <= x <= 144:
    entrance = 4
    if x % 4 == 0:
        floor = (x // 4) - 27
        print('Entrance is', entrance, 'Floor is', floor)
    else:
        floor = ((x // 4) + 1) - 27
        print('Entrance is', entrance, 'Floor is', floor)
elif x > 144:
    print("Flat with this number doesn't exist")
