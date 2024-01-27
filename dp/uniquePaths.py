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