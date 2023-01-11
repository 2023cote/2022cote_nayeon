#baekjoon 1244
n = int(input())
switch = list(map(int, input().split()))

def swap(number):
    if switch[number - 1] == 1:
        switch[number - 1] = 0
    else:
        switch[number - 1] = 1

for i in range(int(input())):
    g, number = map(int, input().split())
    if g == 1:
        while number < n:
            swap(number)
            number += number
    else:
        swap(number)
        if number > 1 and number < n:
            s, e = number - 1, number + 1
        else:
            break
        while switch[s - 1] == switch[e - 1]:
            if s == 1 or e == n:
                break
            swap(s)
            swap(e)
            s -= 1
            e += 1

print(*switch)