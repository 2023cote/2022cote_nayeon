#baekjoon 20291
N = int(input())

arr = []
dict = {}

for i in range(N):
    file = input().split('.')
    arr.append(file[1])

for i in arr:
    if dict.get(i):
        dict[i] += 1
    else:
        dict[i] = 1

dict = sorted(dict.items())

for i,j in dict:
    print(i,j)
#풀이 2
file = []
for i in range(int(input())):
    file.append(input().split('.')[-1])
file.sort()
name = file[0]
cnt = 1
for i in range(1, len(file)):
    if file[i - 1] == file[i]:
        cnt += 1
    else:
        print(name, cnt)
        name = file[i]
        cnt = 1

print(name, cnt)