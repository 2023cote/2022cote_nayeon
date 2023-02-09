r, c = map(int, input().split())
nam = [['.' for _ in range(c + 2)] for _ in range(r + 2)]
fnam = [['.' for _ in range(c + 2)] for _ in range(r + 2)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(1, r + 1):
    string = input()
    for j in range(1, c + 1):
        nam[i][j] = string[j - 1]
minr, maxr = r, 0
minc, maxc = c, 0
for i in range(1, r + 1):
    for j in range(1, c + 1):
        fnam[i][j] = nam[i][j]
        if nam[i][j] == 'X':
            count = 0
            for k in range(4):
                if nam[i + dx[k]][j + dy[k]] == '.':
                    count += 1
            if count >= 3:
                fnam[i][j] = '.'
            else :
                if minr > i:
                    minr = i
                if maxr < i:
                    maxr = i
                if minc > j:
                    minc = j
                if maxc < j :
                    maxc = j

for i in range(minr, maxr + 1):
    print(''.join(fnam[i][minc: maxc + 1]))