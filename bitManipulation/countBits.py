def hammingWeight(n):
    count = 0
    while n:
        n &= (n-1)
        count+=1
    return count

def countBits(n):
    res = []
    for i in range(n+1):
        res.append(hammingWeight(i))
    return res

print(countBits(5))

def countBits2(n):
    dp = [0] * (n+1)
    offset = 1
    for i in range(1, n+1):
        if offset * 2 == i:
            offset = i
        dp[i] = 1 + dp[i-offset]
    return dp

print(countBits2(5))
