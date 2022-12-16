#beakjoon 1931
m_num = int(input())

m_list = []
for i in range(m_num):
    m_list.append(list(map(int, input().split())))
m_list.sort(key=lambda x: x[0])
m_list.sort(key=lambda x: x[1])

count = 0
end = 0
for m in m_list:
    if m[0] >= end:
        count += 1
        end = m[1]

print(count)