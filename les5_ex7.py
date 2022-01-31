import random
zp = []
s = 0
for element in range(12):
    zp.append(random.randint(7500, 15000))
print(zp)
for i in zp:
    s = sum(zp)
print('Middle sum is ', s / 12)
