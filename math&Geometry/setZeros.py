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