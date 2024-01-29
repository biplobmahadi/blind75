def canJump(nums):
    dp = {}
    def rec(i):
        if i == len(nums)-1: return True
        if i in dp: return dp[i]
        for j in range(i+1, i+1+nums[i]):
            if(rec(j)): 
                dp[j] = True
                return True
        dp[i] = False
        return False
    return rec(0)

print(canJump([2,3,1,1,4]))

def canJumpGreedy(nums):
    goal = len(nums) - 1
    for i in range(len(nums)-1, -1, -1):
        if nums[i] + i >= goal:
            goal = i
    return goal == i

print(canJumpGreedy([2,3,1,1,4]))
