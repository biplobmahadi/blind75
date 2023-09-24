def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
            
def twoSum(nums, target):
    map = {}
    for i in range(len(nums)):
        comp = target - nums[i]
        if comp in map:
            return [map[comp], i]
        map[nums[i]] = i
