#baekjoon 1010
n = int(input())

case = []
f = [1]

for i in range(n):
    N, M = map(int, input().split())
    case.append([N, M])

for j in range(1, max(list(zip(*case))[1]) + 1):
    f.append(f[j-1]*j)

for c in case:
    print(int(f[c[1]]/(f[c[0]]*f[c[1]-c[0]])))