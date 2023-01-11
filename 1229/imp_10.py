#baekjoon 4396
n = int(input())
mine = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
result = []
for i in range(1, n + 1):
    a = list(input())
    for j in range(1, n + 1):
        if a[j - 1] == '*':
            mine[i][j] = 1
boom = False
for i in range(1, n + 1):
    a = list(input())
    for j in range(1, n + 1):
        if a[j - 1] == 'x':
            if mine[i][j] == 1:
                boom = True
            else:
                a[j - 1] = mine[i - 1][j - 1] + mine[i - 1][j] + mine[i - 1][j + 1] + mine[i][j - 1] + mine[i][j + 1] + mine[i + 1][j - 1] + mine[i + 1][j] + mine[i + 1][j + 1]
    result.append(a)

if boom == True:
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if mine[i][j] == 1:
                result[i - 1][j - 1] = '*'

for i in range(n):
    print(''.join(str(s) for s in result[i]))