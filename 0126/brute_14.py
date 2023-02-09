#baekjoon 16937 두 스티커
H, W = map(int, input().split())
N = int(input())
stickers = []
for _ in range(N):
    stickers.append(list(map(int, input().split())))
maxS = 0
for i in range(N):
    for j in range(1, N):
        if i == j:
            continue
        s1 = [stickers[i][0], stickers[i][1]]
        s2 = [stickers[j][0], stickers[j][1]]
        S = 0
        if H >= s1[0] and W >= s1[1]:
            if (H - s1[0] >= s2[0] and W >= s2[1]) or (H >= s2[0] and W - s1[1] >= s2[1]) or (H - s1[0] >= s2[1] and W >= s2[0]) or (H >= s2[1] and W - s1[1] >= s2[0]):
                S = s1[0]*s1[1] + s2[0]*s2[1]
                if S > maxS:
                    maxS = S
                continue
        if W >= s1[0] and H >= s1[1]:
            if (W - s1[0] >= s2[0] and H >= s2[1]) or (W >= s2[0] and H - s1[1] >= s2[1]) or (W - s1[0] >= s2[1] and H >= s2[0]) or (W >= s2[1] and H - s1[1] >= s2[0]):
                S = s1[0]*s1[1] + s2[0]*s2[1]
                if S > maxS:
                    maxS = S
print(maxS)