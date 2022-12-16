#baekjoon 1912 ..

n = int(input())
a = list(map(int, input().split()))

max_sum = a[0]

for i in range(1, n):
    a[i] = max(a[i - 1] + a[i], a[i])

print(max(a))