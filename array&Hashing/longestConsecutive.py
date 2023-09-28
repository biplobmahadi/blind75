def longestConsecutive(nums):
    sortedNums =  sorted(nums)
    print(sortedNums)
    if len(sortedNums) == 0:
        return 0
    prev, count, total = sortedNums[0], 1, 1
    for i in range(1, len(sortedNums)):
        if prev + 1 == sortedNums[i] or prev == sortedNums[i]:
            if prev != sortedNums[i]:
                count += 1
        else:
            if count>total:
                total = count
            count = 1
        prev = sortedNums[i]
    if count > total:
        total = count
    return total

nums = [1,2,0,1]
print(longestConsecutive(nums))
