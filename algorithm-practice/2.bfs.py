# 在一个二维列表中，0 代表海洋，1 代表陆地，求连接着的最大的陆地面积

origin = [[0,1,0], [1,1,0], [1,0,1]]
maxArea = 0

# 初始化用来检测的列表，防止重复检测同一块地
visited = []
for i in range(3):
  visited.append([])
  for j in range(3):
    visited[i].append(False)

def bfs(x, y, area):
  global maxArea
  global visited
  global origin
  maxArea = max(area, maxArea)
  ways = [[-1,0], [0,1], [1,0], [0,-1]]
  for way in ways:
    nextX = way[0] + x
    nextY = way[1] + y
    if nextX >= 0 and nextX < 3 and nextY >= 0 and nextY < 3 and visited[nextX][nextY] == False and origin[nextX][nextY] == 1:
      visited[nextX][nextY] = True
      bfs(nextX, nextY, area + 1)
    else:
      pass

for i in range(3):
  for j in range(3):
    if visited[i][j] == False and origin[i][j] == 1:
      visited[i][j] = True
      bfs(i, j, 1)

print(maxArea) # 最大陆地 4