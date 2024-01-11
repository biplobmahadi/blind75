def decode(s):
    dp = {}
    return helper(s, 0, dp)

def helper(s, i, dp):
    if i == len(s): return 1
    if s[i] == '0': return 0
    if i in dp:
        return dp[i]

    dp[i] = helper(s, i+1, dp)
    if (i+1<len(s) and (s[i] == '1' or (s[i] =='2' and s[i+1] in '0123456'))):
        dp[i] += helper(s, i+2, dp)
    return dp[i]

print(decode('10'))

def decodeDp(s):
    last = 0
    secondLast = 1
    for i in range(len(s)-1, -1, -1):
        res = 0
        if s[i] == '0':
            res = 0
        else:
            res = secondLast
        if (i+1<len(s) and (s[i] == '1' or (s[i] =='2' and s[i+1] in '0123456'))):
            res += last
        last = secondLast
        secondLast = res
    return secondLast
print(decodeDp('227'))

