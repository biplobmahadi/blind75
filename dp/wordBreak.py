def wordBreak(s, wordDict):
    dp = {}
    return rec(0, s, wordDict, dp)

def rec(i, s, wordDict, dp):
    if i == len(s): 
        dp[i] = True
        return True
    if i in dp:
        return dp[i]
    for j in range(i, len(s)):
        if s[i:j+1] in wordDict:
            if (rec(j+1, s, wordDict, dp)): 
                dp[i] = True
                return True
    dp[i] = False
    return False

print(wordBreak('leetcode', ['leet', 'code']))
