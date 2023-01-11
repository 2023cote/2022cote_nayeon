#baekjoon 20546
m = int(input())
stock = list(map(int, input().split()))
def BNP() :
    asset = m
    st = 0
    for i in range(14):
        if stock[i] <= asset:
            st += asset // stock[i]
            asset = asset % stock[i]
    return asset + stock[-1] * st

def TIMING() :
    asset = m
    st = 0
    inc = [0 for _ in range(14)]
    for i in range(1, 14):
        if stock[i - 1] < stock[i]:
            if inc[i - 1] > 0:
                inc[i] = inc[i - 1] + 1
            else:
                inc[i] = 1
        elif stock[i - 1] > stock[i]:
            if inc[i - 1] < 0:
                inc[i] = inc[i - 1] - 1
            else:
                inc[i] = -1
        if inc[i] == 3:
            asset += st * stock[i]
            st = 0
        if inc[i] == -3:
            st += asset // stock[i]
            asset = asset % stock[i]
    return asset + stock[-1] * st

jun = BNP()
min = TIMING()

if jun > min:
    print("BNP")
elif jun < min:
    print("TIMING")
else:
    print("SAMESAME")