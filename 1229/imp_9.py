#baekjoon 2578
board = []
for i in range(5):
    a = list(map(int, input().split()))
    board.append(a)
check = [[0 for _ in range(5)] for _ in range(5)]

def bingo(r, c):
    count = 0
    if sum(check[r]) == 5:
        count += 1
    if sum(list(zip(*check))[c]) == 5:
        count += 1
    if r == c:
        for i in range(5):
            if check[i][i] != 1:
                break
            if i == 4:
                count += 1
    if r + c == 4:
        for i in range(5):
            if check[i][4 - i] != 1:
                break
            if i == 4:
                count += 1
    return count
            
            

def search(n):
    for i in range(5):
        for j in range(5):
            if board[i][j] == n:
                return i, j

bingo_count = 0
for i in range(5):
    arr = list(map(int, input().split()))
    for j in range(5):
        n = arr[j]
        r, c = search(n)
        check[r][c] = 1
        bingo_count += bingo(r, c)
        if bingo_count >= 3:
            print(i * 5 + j + 1)
            exit(0)