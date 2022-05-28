size = int(input())
matrix = []

for _ in range(size):
    matrix.append([x for x in input().split(' ')])

symbol = input()
found = False
for row in range(size):
    for col in range(size):
        print(matrix[row][col])
        #if matrix[col][row] == symbol:
            #found = True
            #break

if found:
    print(f'({row}, {col})')
else:
    print(f'{symbol} does not occur in the matrix')

