n = int(input())
mines = [[0 for i in range(n + 2)] for i in range(n + 2)]
for i in range(1, n + 1):
    a = input()
    for j in range(1, n + 1):
        if a[j - 1] == '*':
            mines[i][j] = 1
        else:
            mines[i][j] = 0
fail = 0
result = []
for i in range(1, n + 1):
    check = list(input())
    for j in range(1, n + 1):
        if check[j - 1] == 'x':
            if mines[i][j] == 1:
                fail = 1
            else:
                check[j - 1] = mines[i - 1][j - 1] + mines[i - 1][j] + mines[i - 1][j + 1] + mines[i][j - 1] + mines[i][j + 1] + mines[i + 1][j - 1] + mines[i + 1][j] + mines[i + 1][j + 1]
            
    result.append(check)

if fail == 1:
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if mines[i][j] == 1:
                result[i - 1][j - 1] = '*'

for i in range(n):
    print(''.join(str(s) for s in result[i]))