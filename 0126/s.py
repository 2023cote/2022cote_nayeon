from itertools import product
N = int(input())
P = [0 for _ in range(N)]
I = [0 for _ in range(N)]
for i in range(N):
    P[i], I[i] = map(int, input().split())

candidates = product([1, 0], repeat=N)
maxIncome = 0
for c in candidates:
    time = 0
    income = 0
    for i in range(N):
        if c[i] == 1 and time == 0 and P[i] <= N - i:
            time = P[i]
            income += I[i]
        if time > 0:
            time -= 1
    if maxIncome < income:
        maxIncome = income

print(maxIncome)