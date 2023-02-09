left, right = input().split()
string = input()
keyboard = [['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'], ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'], ['z', 'x', 'c', 'v', 'b', 'n', 'm']]
def find_position(x):
    for i in range(3):
        for j in range(len(keyboard[i])):
            if keyboard[i][j] == x:
                return i, j
time = len(string)
lr, lc = find_position(left)
rr, rc = find_position(right)
for s in string:
    r, c = find_position(s)
    if (r < 2 and c < 5) or (r == 2 and c < 4):
        if left != s:
            time += abs(lr - r) + abs(lc - c)
            left = s
            lr = r
            lc = c
    else:
        if right != s:
            time += abs(rr - r) + abs(rc - c)
            right = s
            rr = r
            rc = c
print(time)