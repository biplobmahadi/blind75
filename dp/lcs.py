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

def lcsBottom(text1, text2):
    M, N = len(text1), len(text2)
    dp = [0] * (N+1)
    for i in range(M-1, -1, -1):
        newDp = [0] * (N+1)
        for j in range(N-1, -1, -1):
            if text1[i] == text2[j]:
                newDp[j] = 1+dp[j+1]
            else:
                newDp[j] = max(newDp[j+1], dp[j])
        dp = newDp
    return dp[0]

print(lcsBottom('abcde', 'ace'))
