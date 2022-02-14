import string


def words(s):
    for i in string.punctuation:
        while i in s:
            s = s.replace(i, ' ')
    s = s.split()
    n = 0
    for i in s:
        n += 1
    return n


s = input('Print text:' + '\n')
print(words(s))
