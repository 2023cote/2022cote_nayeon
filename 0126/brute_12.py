#baekjoon 17626 Four Squares
from math import sqrt
N = int(input())

if sqrt(N) % 1 == 0:
    print(1)
    exit(0)

for i in range(1, int(sqrt(N) + 1)):
    tmp = N - i**2
    if sqrt(tmp) % 1 == 0:
        print(2)
        exit(0)

for i in range(1, int(sqrt(N) + 1)):
    tmp = N - i**2
    for j in range(1, int(sqrt(tmp) + 1)):
        if sqrt(tmp - j**2) % 1 == 0:
            print(3)
            exit(0)
print(4)

#풀이2
from math import sqrt
n = int(input())

if sqrt(n) == int(sqrt(n)):
    print(1)
    exit(0)
m = 4
for i in range(int(sqrt(n)) + 1):
    if sqrt(n - i**2) == int(sqrt(n - i**2)):
        print(2)
        exit(0)
    if m == 3:
        continue
    for j in range(int(sqrt(n - i**2)) + 1):
        if sqrt(n - i**2 - j**2) == int(sqrt(n - i**2 - j**2)):
            m = 3
            break
print(m)