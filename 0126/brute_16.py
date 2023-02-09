from collections import deque

def check_same(board):
    temp = board[0][0]
    for i in range(3):
        for j in range(3):
            if board[i][j] != temp:
                return False
    return True

def calculate(board):
    score = 0
    for i in range(3):
        for j in range(3):
            score = score * 2 + board[i][j]
    return score

def score_to_board(score):
    for i in range(2, -1, -1):
        for j in range(2, -1, -1):
            board[i][j] = score % 2
            score = score // 2

    return board

def find_arr(board):
    global ans
    q = deque()
    score_arr = []

    score = calculate(board)

    q.append((score, 0))

    while q:
        score, count = q.popleft()

        next_board = score_to_board(score)

        if check_same(next_board):
            ans = count
            return

        for i in range(3):
            for j in range(3):
                next_board[i][j] = 0 if next_board[i][j] == 1 else 1

            next_score = calculate(next_board)
            if next_score not in score_arr:
                score_arr.append(next_score)
                q.append((next_score, count+1))

            for j in range(3):
                next_board[i][j] = 0 if next_board[i][j] == 1 else 1

        for i in range(3):
            for j in range(3):
                next_board[j][i] = 0 if next_board[j][i] == 1 else 1

            next_score = calculate(next_board)
            if next_score not in score_arr:
                score_arr.append(next_score)
                q.append((next_score, count+1))

            for j in range(3):
                next_board[j][i] = 0 if next_board[j][i] == 1 else 1

        for i in range(3):
            next_board[i][i] = 0 if next_board[i][i] == 1 else 1

        next_score = calculate(next_board)
        if next_score not in score_arr:
            score_arr.append(next_score)
            q.append((next_score, count+1))

        for i in range(3):
            next_board[i][i] = 0 if next_board[i][i] == 1 else 1

        for i in range(3):
            next_board[2-i][i] = 0 if next_board[2-i][i] == 1 else 1

        next_score = calculate(next_board)
        if next_score not in score_arr:
            score_arr.append(next_score)
            q.append((next_score, count+1))

        for i in range(3):
            next_board[2-i][i] = 0 if next_board[2-i][i] == 1 else 1

    ans = -1

T = int(input())
for _ in range(T):
    board = []
    for i in range(3):
        temp = list(input().split())
        for j in range(3):
            if temp[j] == 'T':
                temp[j] = 1
            else:
                temp[j] = 0
        board.append(temp)
    ans = 0

    find_arr(board)
    print(ans)