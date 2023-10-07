nums = [-1, 0, 1, 2, -1, -4]

def threeSum(nums:list):
    li = []
    nums.sort()
    
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        l, r = i+1, len(nums) - 1
        while r>l:
            total = nums[i] + nums[l] + nums[r]
            if total>0:
                r-=1
            elif total<0:
                l+=1
            else:
                li.append([nums[i], nums[l], nums[r]])
                l+=1
                while nums[l] == nums[l-1] and l<r:
                    l+=1
    return li

print(threeSum(nums))