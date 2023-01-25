#baekjoon 16439 치킨치킨치킨
N, M = map(int, input().split())
pref = []
for i in range(N):
    pref.append(list(map(int, input().split())))

maxPref = 0

for i in range(M):
    for j in range(1, M):
        for k in range(2, M):
            tmp = 0
            for l in range(N):
                tmp += max(pref[l][i], pref[l][j], pref[l][k])
            if tmp > maxPref:
                maxPref = tmp

print(maxPref)