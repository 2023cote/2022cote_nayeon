#baekjoon 14467
N = int(input())
count = 0
cow = [-1 for _ in range(N)]
for _ in range(N):
    i, p = map(int, input().split())
    if cow[i - 1] != p:
        if cow[i - 1] != -1:
            count += 1
            cow[i - 1] = p
        else:
            cow[i - 1] = p

print(count)