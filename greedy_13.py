#baekjoon 21314
mk_str = input()

k_list = []
for pos, char in enumerate(mk_str):
    if char == 'K':
        k_list.append(pos)

max_list = []
min_list = []

if k_list == []:
    for i in range(len(mk_str)): max_list.append(str(1))
    min_list.append(str(10**(len(mk_str) - 1)))
else:
    pre = 0
    for k in k_list:
        max_list.append(str(5*10**(k - pre)))
        if k - pre > 0:
            min_list.append(str(10**(k - pre - 1)))
        min_list.append(str(5))
        pre = k + 1
    if pre != len(mk_str):
        for i in range(len(mk_str) - pre): max_list.append(str(1))
        min_list.append(str(10**(len(mk_str) - pre - 1)))

print("".join(max_list))
print("".join(min_list))