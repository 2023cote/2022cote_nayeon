#baekjoon 14501 퇴사
T = [0]
P = [0]
N = int(input())
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
pay_max = 0
for i in range(2**N):
    t = bin(i)[2:].zfill(N + 1)
    time = 0
    pay = 0
    for j in range(1, N + 1):
        if t[j] == '1':
            if time == 0 and T[j] <= N + 1 - j:
                time = T[j]
                pay += P[j]
            else:
                break
        if time > 0:
            time -= 1
    if pay > pay_max:
        pay_max = pay
print(pay_max)