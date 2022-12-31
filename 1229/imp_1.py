#baekjoon 21611
#미해결

N, M = map(int, input().split())
board = [[] for _ in range(N)]
for i in range(N):
    board[i] = list(map(int, input().split()))
blizard = [[] for _ in range(M)]
for i in range(M):
    blizard[i] = list(map(int, input().split()))
shark = [(N - 1) // 2, (N - 1) // 2]
result = [0, 0, 0]