d = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 15: 'XV', 50: 'L', 100: 'C'}
s = int(input('Input number - '))
if s in d:
    print(d.get(s))
elif s < 4:
    print((d.get(1)) * s)
elif s < 9:
    print((d.get(5)) + (d.get(1) * (s % 5)))
elif s < 14:
    print((d.get(10)) + (d.get(1) * (s % 10)))
elif s < 19:
    print((d.get(10)) + (d.get(5)) + (d.get(1) * (s % 15)))
elif s % 10 == 0 and s < 40:
    print(d.get(10) * (s // 10))
else:
    print('none')
# по такому же принципу можно сделать до 100. Понимаю, что это "костыли" и таким код не должен быть, но оптимизировать код пока не получается