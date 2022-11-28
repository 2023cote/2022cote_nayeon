#baekjoon 10870
n = int(input())

f = []
f.append(0)
f.append(1)

for i in range(2, n + 1):
    f.append(f[i-2] + f[i-1])

print(f[n])