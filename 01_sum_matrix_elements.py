n, m = [int(x) for x in input().split(', ')]

matrix = []
m_sum = 0

for _ in range(n):
    row = [int(x) for x in input().split(', ')]
    matrix.append(row)

for row in range(len(matrix)):
    m_sum += sum(x for x in matrix[row])

print(m_sum)
print(matrix)
