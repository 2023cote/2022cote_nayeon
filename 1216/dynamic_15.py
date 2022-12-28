#baekjoon 21317

n = int(input())
b = []
for i in range(n - 1):
    b.append(list(map(int, input().split())))
k = int(input())

if n == 1:
    print(0)
    exit(0)
d = [0 for i in range(n)]
dk = []
d[1] = b[0][0]
for i in range(2, n):
    d[i] = min(d[i - 1] + b[i - 1][0], d[i - 2] + b[i - 2][1])
    if i >= 3:
        dk.append(d[i] - d[i - 3])
if dk != []:
    if max(dk) > k:
        d[n - 1] -= (max(dk) - k)
print(d[n - 1])