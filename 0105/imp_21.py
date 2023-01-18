#baekjoon 2615
dx, dy = [0, 1, 1, 1], [1, 0, -1, 1]

board = []
visited = [set() for _ in range(4)]

for i in range(19):
  board.append(list(map(int, input().split())))


def check(code, i, j):
  for z in range(4):
    cnt = 1
    res = set()
    res.add((i, j))

    nx, ny = i + dx[z], j + dy[z]

    while 1:
      if 0 <= nx < 19 and 0 <= ny < 19:
        if board[nx][ny] == code and ((nx, ny) not in visited[z]):
          cnt += 1
          res.add((nx, ny))
          visited[z].add((nx, ny))
          nx += dx[z]
          ny += dy[z]
        else:
          if cnt == 5:
            return list(res)
          else:
            break
      else:
        if cnt == 5:
          return list(res)
        break
  return []


def solve():
  for i in range(19):
    for j in range(19):
      if board[i][j] == 1:
        v = check(1, i, j)
        if v:
          return 1, v
      elif board[i][j] == 2:
        v = check(2, i, j)
        if v:
          return 2, v
  return 0, False


code, v = solve()
if v is False:
  print(0)
else:
  tf = 1
  x = v[0][1]
  for i in range(1, 5):
    if x != v[i][1]:
      tf = 0
      break

  if tf:
    v.sort(key=lambda x: (x[0]))
    print(code)
    print(*(v[0][0] + 1, v[0][1] + 1))
  else:
    print(code)
    v.sort(key=lambda x: (x[1]))
    print(*(v[0][0] + 1, v[0][1] + 1))