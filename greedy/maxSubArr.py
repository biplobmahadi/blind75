def maxSubArr(nums):
    sum = nums[0]
    for i in range(len(nums)):
        new = 0
        for j in range(i, len(nums)):
            new += nums[j]
            sum = max(sum, new)
    return sum

print(maxSubArr([-1]))

def maxSubOptimal(nums):
    res = nums[0]
    sum = 0
    for n in nums:
        sum += n
        res = max(res, sum)
        if sum<0:
            sum = 0
    return res

print(maxSubOptimal([-2,1,-3,4,-1,2,1,-5,4]))

