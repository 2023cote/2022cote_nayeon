#baekjoon 13023
N, M = map(int, input().split())
friends = [[] for _ in range(N)]
visited = [False]*N
result = False

for i in range(M):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

def dfs(depth, x):
    global result
    if depth == 4:
        print(1)
        exit(0)
    for i in friends[x]:
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, i)
            visited[i] = False

chain = []
for i in range(N):
    visited[i] = True
    dfs(0, i)
    visited[i] = False

print(0)