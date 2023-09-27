def productExceptSelf(nums):
    ans = []
    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            if i!=j:
                product *= nums[j]
        ans.append(product)
    return ans

def productExceptSelf2(nums):
    ans, all = [], 1
    zeros = []
    for i, n in enumerate(nums):
        if n == 0: zeros.append(i)
        else: all *= n
    if len(zeros) > 1:
        ans = [0]*len(nums)
    else:
        for i in nums:
            if len(zeros) ==1:
                if i == 0:
                    product = all
                    ans.append(product)
                else: ans.append(0)
            else: 
                product = all / i
                ans.append(product)
    return ans
