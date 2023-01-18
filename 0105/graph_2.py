import sys
sys.setrecursionlimit(300000)

def dfs(node):
    for n in graph[node]:
        if p[n] == 0:
            p[n] = node
            dfs(n)

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
p = [0]*(N+1)
dfs(1)
for i in range(2, N+1):
    print(p[i])