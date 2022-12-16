#baekjoon 9095
n = int(input())
list_n = []
for i in range(n):
    list_n.append(int(input()))
m = max(list_n)

d = [0] * (m + 1)
d[0] = 1
d[1] = 1
d[2] = 2
for i in range(3, m + 1):
    d[i] += d[i - 3]
    d[i] += d[i - 2]
    d[i] += d[i - 1]

for i in list_n:
    print(d[i])