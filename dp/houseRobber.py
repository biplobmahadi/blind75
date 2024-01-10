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

def rob2(nums):
    N = len(nums)
    if N == 1: return nums[0]
    if N == 2: return max(nums[0], nums[1])

    one, two, three = 0, nums[0], nums[1]
    for i in range(2, N):
        res = nums[i] + max(one, two)
        one = two
        two = three
        three = res
    return max(two, three)

print(rob2([1,7,9,2]))