#baekjoon 21918
N, M  = map(int, input().split())
state = list(map(int, input().split()))

for _ in range(M):
    a, b, c = map(int, input().split())
    if a == 1:
        state[b - 1] = c
    elif a == 2:
        for i in range(b - 1, c):
            if state[i] == 1:
                state[i] = 0
            else:
                state[i] = 1
    elif a == 3:
        for i in range(b - 1, c):
            if state[i] == 1:
                state[i] = 0
    else:
        for i in range(b - 1, c):
            if state[i] == 0:
                state[i] = 1
print(*state)