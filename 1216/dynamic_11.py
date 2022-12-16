#baekjoon 2407
n, m = map(int, input().split())

d = [1 for i in range(n)]
for i in range(1, n):
    d[i] = d[i - 1] * (i + 1)

print(d[n - 1]//d[m - 1]//d[n - m - 1])