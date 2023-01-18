#baekjoon 16918
from collections import deque

def loc_bomb():
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 'O':
                bomb.append((i, j))

def full_bomb():
    for i in range(r):
        for j in range(c):
            if graph[i][j] != "O":
                graph[i][j] = "O"

def bombs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while bomb:
        a, b = bomb.popleft()
        graph[a][b] = "."

        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]

            if 0 <= x < r and 0 <= y < c:
                if graph[x][y] == "O":
                    graph[x][y] = "."


r, c, n = map(int, input().split())
graph = [list(map(str, input().strip())) for _ in range(r)]
n -= 1

while n:
    bomb = deque()
    loc_bomb()
    full_bomb()

    n -= 1
    if n == 0:
        break

    bombs()
    n -= 1

for i in graph:
    print("".join(i))