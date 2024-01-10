dp = {}
def climb(n):
    if n == 0:
        return 1
    if n<0:
        return 0
    if n in dp:
        return dp[n]
    dp[n] = climb(n-1) + climb(n-2)
    return dp[n]

print(climb(3))

def bottomUp(n):
    dpOne = 1
    dpTwo = 1
    for _ in range(2, n+1):
        dp = dpOne+dpTwo
        dpOne = dpTwo
        dpTwo = dp
    return dpTwo

print(bottomUp(3))
