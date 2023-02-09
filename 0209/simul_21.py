from collections import deque
N = int(input())
M = int(input())
l = list(map(int, input().split()))
vote = [0 for _ in range(101)]
frame = deque()
for k in l:
    vote[k] += 1
    if k not in frame:
        if len(frame) == N:
            min_idx = 0
            for i in range(N):
                if vote[frame[i]] < vote[frame[min_idx]]:
                    min_idx = i
            vote[frame[min_idx]] = 0
            del frame[min_idx]
        frame.append(k)
print(*sorted(frame))