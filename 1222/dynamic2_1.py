#baekjoon 21921

N, X = map(int, input().split())
visits = list(map(int, input().split()))

tmp = sum(visits[0:X])
max = tmp
count = 1

for i in range(X, len(visits)):
    tmp = tmp - visits[i - X] + visits[i]
    if tmp > max:
        max = tmp
        count = 1
    elif tmp == max:
        count += 1

if max == 0:
    print("SAD")
    exit(0)

print(max)
print(count)