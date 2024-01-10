def rob(nums):
    return max(nums[0], helper(nums[1:]), helper(nums[:-1]))

def helper(nums):
    one = 0
    two = 0
    for n in nums:
        tmp = max(n+one, two)
        one = two
        two = tmp
    return two

print(rob([2, 3, 2]))