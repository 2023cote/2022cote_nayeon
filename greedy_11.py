#baekjoon 1541
math_str = input()

idx = []

for pos, char in enumerate(math_str):
    if char == '+' or char == '-':
        idx.append(char)

math_str = math_str.replace('+', ' ').replace('-', ' ')
n_list = list(map(int, math_str.split()))

res = n_list[0]
m = False
for i in range(len(idx)):
    if idx[i] == '-':
        m = True
    if m == False:
        res += n_list[i+1]
    else:
        res -= n_list[i+1]

print(res)