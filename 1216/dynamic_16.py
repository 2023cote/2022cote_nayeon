#baekjoon 22857

n, k = map(int, input().split())
seq = list(map(int, input().split()))

p1, p2 = (0, 0)
odd_num = 1 if seq[p1] & 1 == 1 else 0
max_length = 0

while p1 < n and p2 < n:
    index_error = False

    while odd_num <= k:
        try:
            p2 += 1
            if seq[p2] & 1 == 1:
                odd_num += 1
        except IndexError:
            index_error = True
            break

    if not index_error:
        odd_num -= 1
    p2 -= 1

    max_length = max(max_length, p2 - p1 + 1 - odd_num)

    if seq[p1] & 1 == 1:
        odd_num -= 1
    p1 += 1

print(max_length)