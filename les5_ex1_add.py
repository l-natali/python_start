for i in range(1, 100):
    a = 2
    while a < i:
        if i % a == 0:
            break
        a += 1
    else:
        print(i)
