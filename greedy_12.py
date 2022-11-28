#baekjoon 16953
a, b = map(int, input().split())

i = 0
while(a != b):
    if b % 2 == 0:
        b /= 2
    else:
        b = (b - 1) / 10
    i += 1
    if b < 1:
        i = -2
        break

print(i + 1)