import sys
from itertools import combinations

def check(li):
    global answer
    visited = [] 
    total = 0
    for r, c in li:
        visited.append((r, c))
        total += fields[r][c]
        for idx in range(4):
            nr = r + d[idx][0]
            nc = c + d[idx][1]
            if (nr, nc) not in visited:
                visited.append((nr, nc))
                total += fields[nr][nc]
            else:
                return
    answer = min(answer, total)

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

N = int(input())
answer = int(1e9)
fields = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
candidates = [(r, c) for r in range(1, N-1) for c in range(1, N-1)]

for li in combinations(candidates, 3):
    check(li)
print(answer)