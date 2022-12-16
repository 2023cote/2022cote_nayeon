#baekjoon 17626
#미해결
import math

x = int(input())
n = 2
list_n = [1]
while True:
    tmp = n**2
    if tmp > x:
        break
    list_n.append(tmp)
    n += 1

#x가 거듭제곱인 경우2
if x == list_n[-1]:
    print(1)
    exit(0)
    
#2개 이상의 거듭제곱으로 표현되는 경우
