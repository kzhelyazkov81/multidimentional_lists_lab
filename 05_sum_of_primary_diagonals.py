size = int(input())
matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split(' ')])

pd_sum = 0
for i in range(size):
    pd_sum += matrix[i][i]

print(pd_sum)
