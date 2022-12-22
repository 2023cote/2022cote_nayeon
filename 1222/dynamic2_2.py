#baekjoon 21921

N, K = map(int, input().split())
a = list(map(int, input().split()))
cnt = [0 for _ in range(max(a) + 1)]

i = 0
max = 1

for j in range(1, N + 1):
    cnt[a[j - 1]] += 1
    if cnt[a[j - 1]] > K:
        while a[i] != a[j - 1]:
            cnt[a[i]] -= 1
            i += 1
        cnt[a[j - 1]] -= 1
        i += 1
    else:
        if max < j - i:
            max = j - i

print(max)