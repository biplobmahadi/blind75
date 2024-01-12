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