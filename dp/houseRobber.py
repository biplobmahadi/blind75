def rob(nums):
    n = len(nums)-1
    dp = {}
    return robber(n, nums, dp)

def robber(n, nums, dp):
    if n<0: return 0
    if n not in dp:
        dp[n] = max(nums[n] + robber(n-2, nums, dp),
               (nums[n-1] if n-1>=0 else 0) + robber(n-3, nums, dp))
    return dp[n]

print(rob([1,7,9,2]))