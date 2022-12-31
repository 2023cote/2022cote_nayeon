#baekjoon 20546
m = int(input())
arr = list(map(int, input().split()))
jm, sm, j, s, status = m, m, 0, 0, [0, '']
yesterday = arr[0]


for i in range(14):
    # 준현
    if jm // arr[i] != 0:
        temp = jm // arr[i]
        j += (jm // arr[i])
        jm -= temp * arr[i]

    # 성민
    change = 0
    if yesterday < arr[i]:
        if status[1] == '-':
            change = 1
        status[1] = '+'

    elif yesterday > arr[i]:
        if status[1] == '+':
            change = 1
        status[1] = '-'

    yesterday = arr[i]

    if change:
        status[0] = 1
    elif status[1] != '':
        status[0] += 1

    if status[0] >= 3:
        if status[1] == '+':
            if sm // arr[i] != 0:
                sm += s * arr[i]
                s = 0

        if status[1] == '-':
            temp = sm // arr[i]
            s += (sm // arr[i])
            sm -= temp * arr[i]


last_day = arr[-1]
sm += (s * last_day)
jm += (j * last_day)

if sm == jm:
    print("SAMESAME")
elif sm > jm:
    print("TIMING")
else:
    print("BNP")