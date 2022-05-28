def find_symbol(symbol, matrix):
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == symbol:
                return row, col


size = int(input())
matrix = []

for _ in range(size):
    matrix.append([x for x in input()])

symbol = input()
result = find_symbol(symbol, matrix)

if result:
    row_index, col_index = result
    print(f'({row_index}, {col_index})')
else:
    print(f'{symbol} does not occur in the matrix')
