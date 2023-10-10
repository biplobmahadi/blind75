def findMin(nums):
    res = nums[0]
    for i in range(1, len(nums)):
        res = min(res, nums[i])
    return res

def findMinOptimal(nums):
    left, right, res = 0, len(nums) - 1, nums[0]
    while right>=left:
        mid = (left + right) // 2
        res = min(res, nums[mid])
        if nums[mid] > nums[right]:
            left = mid +1
        else:
            right = mid - 1
    return res

print(findMinOptimal([6, 1, 2, 3, 4, 5]))