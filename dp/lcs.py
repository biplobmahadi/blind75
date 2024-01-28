def lcs(text1, text2):
    dp = [[-1]*len(text2) for _ in range(len(text1))]
    def rec(i, j):
        if i == len(text1) or j == len(text2): return 0
        if dp[i][j] != -1: return dp[i][j]
        if text1[i] == text2[j]: return 1 + rec(i+1, j+1)
        else:  
            dp[i][j] = max(rec(i, j+1), rec(i+1, j))
            return dp[i][j]
    return rec(0, 0)

print(lcs('abcde', 'ace'))
