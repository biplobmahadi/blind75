def search(nums, target):
    for i, n in enumerate(nums):
        if n == target:
            return i
    return -1

def searchOptimal(nums, target):
    l, r = 0, len(nums)-1
    while r>=l:
        m = (l+r)//2
        if nums[m] == target:
            return m
        if nums[m] > nums[r]:
            if target>=nums[l] and target<=nums[m]: r=m-1
            else: l=m+1
        else:
            if target<=nums[r] and target>=nums[m]: l=m+1
            else: r = m-1
    return -1

print(search([6, 0, 1, 3, 4, 5], 0))
print(searchOptimal([6, 0, 1, 3, 4, 5], 0))
