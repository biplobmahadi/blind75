def uniq(m, n):
    dp = [[-1]*n for _ in range(m)]
    def paths(r, c):
        if r == m or c == n: return 0
        if r == m-1 and c == n-1: return 1
        if dp[r][c] != -1: return dp[r][c]
        count = 0
        count+= paths(r+1, c)
        count+= paths(r, c+1)
        dp[r][c] = count
        return dp[r][c]
    return paths(0, 0)

print(uniq(3, 7))

def uniqPaths(m, n):
    dp = [[0]*(n+1) for _ in range(m+1)]
    dp[m-1][n-1] = 1
    for r in range(m-1, -1,-1):
        for c in range(n-1, -1,-1):
            if dp[r][c] == 0:
                dp[r][c] = dp[r+1][c] + dp[r][c+1]
    return dp[0][0]

print(uniqPaths(3, 7))

def uniqPathsMemo(m, n):
    dpLast = [0] * (n)
    dp = [0] * (n)
    dp[n-1] = 1
    for r in range(m-1, -1,-1):
        for c in range(n-2, -1,-1):
            dp[c] = dpLast[c] + dp[c+1]
        dpLast = dp
    return dp[0]

print(uniqPathsMemo(3, 7))
