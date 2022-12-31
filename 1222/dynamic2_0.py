#baekjoon 11728
n, m = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = []

ptr1 = 0
ptr2 = 0

for i in range(len(A) + len(B)):
    if ptr1 == len(A):
        C = C + B[ptr2:len(B)]
        break
    if ptr2 == len(B):
        C = C + A[ptr1:len(A)]
        break
    if A[ptr1] <= B[ptr2]:
        C.append(A[ptr1])
        ptr1 += 1
    else:
        C.append(B[ptr2])
        ptr2 += 1

print(*C)