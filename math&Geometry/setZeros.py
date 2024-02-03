def setZeros(matrix):
    row, col = len(matrix), len(matrix[0])
    pos = []
    for r in range(row):
        for c in range(col):
            if matrix[r][c] == 0:
                pos.append([r, c])
    for r, c in pos:
        for i in range(c+1, col):
            matrix[r][i] = 0
        for i in range(c-1, -1, -1):
            matrix[r][i] = 0
        for i in range(r+1, row):
            matrix[i][c] = 0
        for i in range(r-1, -1, -1):
            matrix[i][c] = 0

def setZero(matrix):
    ROWS, COLS = len(matrix), len(matrix[0])
    zeroRow = False
    for r in range(ROWS):
        for c in range(COLS):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                if r>0: matrix[r][0] = 0
                else: zeroRow = True
    for r in range(1, ROWS):
        for c in range(1, COLS):
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0
    if matrix[0][0] == 0:
        for r in range(ROWS):
            matrix[r][0] = 0
    if zeroRow:
        for c in range(COLS):
            matrix[0][c] = 0
