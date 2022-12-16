#baekjoon 2579
n = int(input())
list_n = [0 for i in range(301)]
for i in range(n):
    list_n[i + 1] = int(input())

d = [0 for i in range(301)]
d[1] = list_n[1]
d[2] = list_n[1] + list_n[2]
d[3] = max(list_n[1] + list_n[3], list_n[2] + list_n[3])
for i in range(4, n + 1):
    d[i] = max(d[i - 2] + list_n[i], d[i - 3] + list_n[i - 1] + list_n[i])

print(d[n])