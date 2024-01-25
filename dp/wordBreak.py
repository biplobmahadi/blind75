def wordBreak(s, wordDict):
    return rec(0, s, wordDict)

def rec(i, s, wordDict):
    if i == len(s): return True
    for j in range(i, len(s)):
        if s[i:j+1] in wordDict:
            if (rec(j+1, s, wordDict)): return True
    return False

print(wordBreak('leetcod', ['leet', 'code']))
