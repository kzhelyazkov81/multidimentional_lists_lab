rows, columns = [int(x) for x in input().split(', ')]
matrix = []

for _ in range(rows):
    row = [int(x) for x in input().split(' ')]
    matrix.append(row)

for column in range(columns):
    column_sum = 0
    for row in range(rows):
        column_sum += matrix[row][column]
    print(column_sum)
