def findMin(nums):
    res = nums[0]
    for i in range(1, len(nums)):
        res = min(res, nums[i])
    return res

