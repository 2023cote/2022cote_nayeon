#baekjoon 20436
def find_loc(word):
    keyboard = [
        ['q','w','e','r','t','y','u','i','o','p'],
        ['a','s','d','f','g','h','j','k','l'],
        ['z','x','c','v','b','n','m']
    ]

    for i, key in enumerate(keyboard):
        if word in key:
            y = i
            x = key.index(word)
            return x, y


sl, sr = map(str, input().split())
data = input()
result = 0

consonant = "qwertasdfgzxcv"

for d in data:
    
    if sl == d or sr == d:
        result += 1
  
    else:
        slx, sly = find_loc(sl)
        srx, sry = find_loc(sr)
        dx, dy = find_loc(d)

        if d in consonant:
            result += abs(slx-dx) + abs(sly-dy) + 1
            sl, slx, sly = d, dx, dy
        else:
            result += abs(srx-dx) + abs(sry-dy) + 1
            sr, srx, sry = d, dx, dy

print(result)