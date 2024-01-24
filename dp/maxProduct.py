def maxProduct(nums):
    res = nums[0]
    for i, n in enumerate(nums):
        prod = n
        res = max(res, prod)
        for j in range(i+1, len(nums)):
            curr = nums[j]
            prod *= curr
            res = max(res, prod)
    return res

print(maxProduct([2, 3, -2, 4]))

def maxProductOptimal(nums):
    res = nums[0]
    currMax, currMin = 1, 1

    for n in nums:
        tmp = currMax * n
        currMax = max(tmp, currMin*n, n)
        currMin = min(tmp, currMin*n, n)
        res = max(res, currMax)
    return res

print(maxProductOptimal([2, 3, -2, 4]))
