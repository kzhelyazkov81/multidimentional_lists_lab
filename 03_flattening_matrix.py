rows = int(input())
matrix = []
flattened_matrix = []

for _ in range(rows):
    row = [int(x) for x in input().split(', ')]
    matrix.append(row)

for row in range(len(matrix)):
    for x in matrix[row]:
        flattened_matrix.append(x)

print(flattened_matrix)
