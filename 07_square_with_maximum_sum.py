def submatrix_sum(matrix, start_row, start_column):
    result = 0
    for i in range (start_row, start_row+2):
        for j in range(start_column, start_column+2):
            result += matrix[i][j]
    return result


def submatrix(matrix, start_row, start_column):
    result = []
    for row in range(start_row, start_row+2):
        result.append(matrix[row][start_column:start_column+2])
    return result

rows, columns = [int(x) for x in input().split(', ')]

matrix = []
for row in range(rows):
    matrix.append([int(x) for x in input().split(', ')])


maximum_sum = float('-inf')
max_submatrix = []
for subrow in range(rows-1):
    for subcolumn in range(columns-1):
        sub_sum = submatrix_sum(matrix, subrow, subcolumn)
        if sub_sum > maximum_sum:
            maximum_sum = sub_sum
            max_submatrix = submatrix(matrix, subrow, subcolumn)


for row in max_submatrix:
    print(' '.join(str(x) for x in row))
print(maximum_sum)



