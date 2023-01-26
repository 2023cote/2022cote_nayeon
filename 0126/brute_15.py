#baekjoon 16508 전공책
word = input()
N = int(input())
price = []
books = []
for i in range(N):
    p, b = input().split()
    price.append(int(p))
    books.append(b)
minCost = sum(price) + 1
for i in range(1, 2**N):
    check = bin(i)[2:].zfill(N)
    S = [0 for _ in range(len(word))]
    cost = 0
    for j in range(N):
        if check[j] == '1':
            cost += price[j]
            for c in books[j]:
                for k in range(len(word)):
                    if word[k] == c and S[k] == 0:
                        S[k] = 1
    if sum(list(S)) == len(word) and minCost > cost:
        minCost = cost
if minCost == sum(price) + 1:
    print(-1)
else:
    print(minCost)