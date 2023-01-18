#baekjoon 17836
from collections import deque
N, M, T = map(int, input().split())
l = []
INF = 2147000000
dx = [0,0,1,-1]
dy = [1,-1,0,0]

for _ in range(N):
    l.append(list(map(int, input().split())))

time = [[INF for _ in range(M + 2)]for _ in range(N + 2)]

dq = deque([])
time[1][1] = 0
dq.append([1,1])
gram = False
while dq:
    x, y = dq.popleft()
    for i in range(4):
        if 0 < x + dx[i] < N + 1 and 0 < y + dy[i] < N + 1 and time[x + dx[i]][y + dy[i]] == INF:
            if l[x + dx[i] - 1][y + dy[i] - 1] != 1:
                time[x + dx[i]][y + dy[i]] = time[x][y] + 1
                dq.append([x + dx[i], y + dy[i]])
                if l[x + dx[i] - 1][y + dy[i] - 1] == 2:
                    gram = [x + dx[i],y + dy[i]]

if gram != False:
    time[N][M] = min(time[N][M], time[gram[0]][gram[1]] + N + M - gram[0] - gram[1])
if time[N][M] != INF:
    print(time[N][M])
else:
    print("fail")