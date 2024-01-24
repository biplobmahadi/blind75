import math

def topDown(coins, amount):
    if amount < 1: return 0
    dp = {}
    def dfs(a):
        if a in dp: return dp[a]
        if a == 0: return 0
        val = math.inf
        for n in coins:
            if a - n >= 0:
                val = min(val, dfs(a - n))
        dp[a] = val + 1
        return dp[a]
    dfs(amount)
    return dp[amount] if dp[amount] != math.inf else -1

print(topDown([1], 0))

def bottomUp(coins, amount):
    if amount < 1: return 0
    dp = [math.inf] * (amount+1)
    dp[0] = 0
    for a in range(1, amount+1):
        val = math.inf
        for c in coins:
            if a - c>= 0:
                val = min(dp[a-c], val)
        dp[a] = val + 1
    return dp[amount] if dp[amount] != math.inf else -1

print(bottomUp([1], 0))