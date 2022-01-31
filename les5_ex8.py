matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
sm = 1
print(matrix[0][0:4], matrix[1][0:4], matrix[2][0:4], matrix[3][0:4], sep='\n')
s = list(map(sum, matrix))
for i in s:
    sm = sum(s)
print('Matrix sum = ', sm)
