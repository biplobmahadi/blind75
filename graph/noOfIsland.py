grid1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

from collections import deque

def numIslands(grid):
    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            count += bfs(grid, row, col)
    return count

directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def bfs(grid, r, c):
    if grid[r][c] == '0':
        return 0
    ROW, COL = len(grid), len(grid[0])
    q = deque()
    q.append((r, c))
    grid[r][c] = '0'
    while q:
        row, col = q.popleft()

        for rd, cd in directions:
            nowR = row + rd
            nowC = col + cd
            if (nowR >= 0 and nowC >= 0 and nowR < ROW and
                nowC < COL and grid[nowR][nowC] == '1'):
                q.append((nowR, nowC))
                grid[nowR][nowC] = '0'
    return 1

print(numIslands(grid2))