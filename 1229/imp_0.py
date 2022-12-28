#baekjoon
N = int(input())
arr = []

near = [[0 for _ in range(N + 2)] for _ in range(N + 2)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == 1 or i == N:
            if j == 1 or j == N:
                near[i][j] = 2
            else:
                near[i][j] = 3
        else:
            near[i][j] = 4

seat = [[0 for _ in range(N + 2)] for _ in range(N + 2)]

for i in range(N**2):
    arr.append(list(map(int, input().split())))
    