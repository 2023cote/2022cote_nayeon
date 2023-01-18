#baekjoon 2798
N, M = map(int, input().split())
l = list(map(int, input().split()))
S = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            tmp = l[i] + l[j] + l[k]
            if tmp <= M:
                S = max(tmp, S)
print(S)