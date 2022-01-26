x = [0, 5, 2, 4, 7, 1, 3, 19]
i = 0
j = 0
while i < len(x):
    for element in x:
        if element % 2:
            print(element)
            j += 1
        i += 1
print('Kolichestvo nechetnyh chysel ', j)

#не совсем поняла условие - надо вывести нечетные или посчитать их количество? поэтому и вывела и посчитала