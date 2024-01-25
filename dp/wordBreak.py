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


def wordBreakOptimal(s, wordDict):
    dp = [False] * (len(s)+1)
    dp[len(s)] = True

    for i in range(len(s)-1, -1, -1):
        for w in wordDict:
            if len(w) <= len(s) - i and s[i:i+len(w)] == w:
                dp[i] = dp[i+len(w)]
            if dp[i]:
                break
    return dp[0]

print(wordBreakOptimal('leetcode', ['leet', 'code']))
