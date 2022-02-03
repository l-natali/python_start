name = input('Enter your name - ')
if name.isalpha() and name[0].isupper() and name[1:].islower():
    print('Name is correct')
else:
    print('Name does not correct')
