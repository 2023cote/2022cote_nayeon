#baekjoon 18312
N, K = map(int, input().split())
H = 0
M = 0
S = 0
count = 0
while H <= N:
    if K in list(map(int, format(H, '02'))) or K in list(map(int, format(M, '02'))) or K in list(map(int, format(S, '02'))):
        count += 1
    S += 1
    if S == 60:
        S = 0
        M += 1
    if M == 60:
        M = 0
        H += 1
print(count)