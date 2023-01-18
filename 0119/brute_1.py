#baekjoon 2231
import math
N = int(input())
t = 1
while N//t != 0:
    t *= 10
t = min(N - 1, int(math.log10(t)))
result = max(0, N - t * 9)
while result < N:
    if result + sum(list(map(int, str(result)))) == N:
        print(result)
        exit(0)
    result += 1
print(0)