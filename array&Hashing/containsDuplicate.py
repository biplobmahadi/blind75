def containsDuplicate(nums: list):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

def containsDuplicateOptimal(nums: list):
    hashset = set()
    for n in nums:
        if n in hashset: return True
        hashset.add(n)
    return False