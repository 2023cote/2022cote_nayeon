def rotate_1(m, n):
    tmp = list(zip(*m))[n//2]
    for i in range(n):
        m[i][n//2] = m[i][n - i - 1]
        m[i][n - i - 1] = m[n//2][n - i - 1]
        m[n//2][i] = m[i][i]
        m[i][i] = tmp[i]
    return m

def rotate_2(m, n):
    tmp = list(zip(*m))[n//2]
    for i in range(n):
        m[i][n//2] = m[i][n - i - 1]
        m[i][n - i - 1] = m[n//2][n - i - 1]
        m[n//2][i] = m[i][i]
        m[i][i] = tmp[i]
    return m


for _ in range(int(input())):
    n, a = map(int, input().split())
    m = []
    for _ in range(n):
        arr = list(map(int, input().split()))
        m.append(arr)
    if a > 0:
        for i in range(a//45):
            m = rotate_1(m, n)
    elif a < 0:
        for i in range(abs(a)//45):
            m = rotate_2(m, n)
    for i in range(n):
        print(*m[i])