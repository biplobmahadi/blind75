import math

def topDown(coins, amount):
    res = [math.inf]
    def dfs(i, c, a):
        if i == len(coins): return
        if a == 0: res[0] = min(res[0], c)
        dfs(i+1, c, a)
        if a - coins[i] >= 0:
            dfs(i, c+1, a - coins[i])
            
    dfs(0, 0, amount)
    return res[0] if res[0] != math.inf else -1

print(topDown([1], 0))