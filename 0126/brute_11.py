#baekjoon 2503 숫자야구
N = (int(input()))
nums = []
strike = []
ball = []

for i in range(N):
    num, st, ba = map(int, input().split())
    nums.append(str(num))
    strike.append(st)
    ball.append(ba)

cnt = 0
for i in range(1, 10):
    for j in range(1, 10):
        if i == j:
            continue
        for k in range(1, 10):
            if i == k or j == k:
                continue
            flag = True
            for l in range(N):
                s, b = 0, 0
                if flag == False:
                    break
                if int(nums[l][0]) == i:
                    s += 1
                elif int(nums[l][0]) == j or int(nums[l][0]) ==k:
                    b += 1
                if int(nums[l][1]) == j:
                    s += 1
                elif int(nums[l][1]) == i or int(nums[l][1]) ==k:
                    b += 1
                if int(nums[l][2]) == k:
                    s += 1
                elif int(nums[l][2]) == i or int(nums[l][2]) ==j:
                    b += 1
                if s != strike[l] or b != ball[l]:
                    flag = False
            if flag == True:
                cnt += 1
print(cnt)

# from itertools import permutations

# N = int(input())
# li = []
# strike = [0 for _ in range(N)]
# ball = [0 for _ in range(N)]

# for i in range(N):
#     n, strike[i], ball[i] = map(int, input().split())
#     li.append(str(n))

# cnt = 0
# candidates = permutations([i for i in range(1, 10)], 3)
# for c in candidates:
#     flag = True
#     for i in range(N):
#         s = 0
#         b = 0
#         for j in range(3):
#             if int(li[i][j]) == c[j]:
#                 s += 1
#             elif int(li[i][(j + 1)%3]) == c[j] or int(li[i][(j + 2)%3]) == c[j]:
#                 b += 1
#         if strike[i] != s or ball[i] != b:
#             flag = False
#             break
#     if flag == True:
#         cnt += 1
# print(cnt)