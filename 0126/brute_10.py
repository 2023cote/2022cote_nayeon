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

##풀이2
# from itertools import combinations
# N, M  = map(int, input().split())
# pref = []
# for _ in range(N):
#     pref.append(list(map(int, input().split())))

# Coms = combinations([i for i in range(M)], 3)
# maxS = 0
# for c in Coms:
#     S = 0
#     for i in range(3):
#         S += max(pref[i][c[0]], pref[i][c[1]], pref[i][c[2]])
#     if maxS < S:
#         maxS = S
# print(maxS)