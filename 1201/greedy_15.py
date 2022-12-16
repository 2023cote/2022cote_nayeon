#baekjoon 11000
from heapq import heappush, heappop
n = int(input())

c_list = []
for i in range(n):
    c_list.append(list(map(int,input().split())))

c_list.sort()

room = []
heappush(room, c_list[0][1])
c_list = c_list[1:]

for c in c_list:
    if room[0] > c[0]:
        heappush(room, c[1])
    else:
        heappop(room)
        heappush(room, c[1])
        
print(len(room))