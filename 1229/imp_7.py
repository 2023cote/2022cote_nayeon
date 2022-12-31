#baekjoon 14467
n = int(input())
 
pos = {}
count = 0
 
for i in range(n):
    a,b = map(int, input().split())
    if a not in pos:
        pos[a] = b
    else:
        if pos[a] != b:
            count +=1
            pos[a] = b
 
print(count)