a, b, c = int(input('a=')), int(input('b=')), int(input('c='))
if a + b > c and a + c > b and b + c > a:
    print('Triangle is exist')
else:
    print('Triangle does not exist')
