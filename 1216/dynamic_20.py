#baekjoon 10844
n = int(input())
st = [0]*10
dp = [0]*10

for i in range(1, 10):
    st[i] = 1

for _ in range(n - 1):
    dp[0] = st[1]
    dp[9] = st[8]
    for i in range(1, 9):
        dp[i] = st[i - 1] + st[i + 1]
    st = list(dp)

print(sum(dp) % 1000000000)