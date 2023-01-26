from itertools import combinations

N = int(input())
arr = [list(map(int, input().split(" "))) for _ in range(N)]
coms = [combinations(arr, i) for i in range(1, N+1)]
ans = 1000000000
for com in coms:
    for t in com:
        S, B = 1, 0
        for s, b in t:
            S *= s
            B += b
        ans = min(ans, abs(S-B))
print(ans)