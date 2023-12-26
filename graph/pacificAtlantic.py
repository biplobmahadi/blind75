from collections import deque

def pacificAtlantic(heights):
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    ROWS, COLS = len(heights), len(heights[0])

    def bfs(r, c):
        q = deque()
        q.append((r, c))
        visited = set()
        visited.add((r,c))
        isPaci = False
        isAtlan = False
        while q:
            row, col = q.popleft()
            if inPacific(row, col):
                isPaci = True
            if inAtlantic(row, col):
                isAtlan = True
            if isPaci and isAtlan:
                return True
            for dr, dc in directions:
                nwR = dr+row
                nwC = dc + col
                if (nwR>=0 and nwC>=0 and nwR<ROWS and 
                    nwC<COLS and heights[nwR][nwC]<=heights[row][col] and
                    (nwR, nwC) not in visited):
                    q.append((nwR, nwC))
                    visited.add((nwR, nwC))
        return False
    
    def inPacific(r, c):
        if (r==0 or c ==0):
            return True
        else:
            return False
    def inAtlantic(r, c):
        if (r==ROWS-1 or c ==COLS-1):
            return True
        else:
            return False
    
    res = []
    for row in range(ROWS):
        for col in range(COLS):
            if(bfs(row, col)):
                res.append([row, col])
    return res

heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(pacificAtlantic(heights))

def pacificAtlanticOptimal(heights):
    ROWS, COLS = len(heights), len(heights[0])
    atl, pac = set(), set()

    def dfs(ocean, r, c, prevHeight):
        if (r<0 or c<0 or r>=ROWS or c>=COLS or 
            ((r,c) in ocean) or heights[r][c] < prevHeight):
            return 
        ocean.add((r, c))
        dfs(ocean, r+1, c, heights[r][c])
        dfs(ocean, r-1, c, heights[r][c])
        dfs(ocean, r, c+1, heights[r][c])
        dfs(ocean, r, c-1, heights[r][c])

    for r in range(ROWS):
        dfs(pac, r, 0, heights[r][0])
        dfs(atl, r, COLS-1, heights[r][COLS-1])
    
    for c in range(COLS):
        dfs(pac, 0, c, heights[0][c])
        dfs(atl, ROWS-1, c, heights[ROWS-1][c])

    res = []
    for row in range(ROWS):
        for col in range(COLS):
            if (row, col) in pac and (row, col) in atl:
                res.append([row, col])
    return res

print(pacificAtlanticOptimal(heights))