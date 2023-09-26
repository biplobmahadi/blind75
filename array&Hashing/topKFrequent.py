def topKFrequent(nums: list, k):
    map, count = {}, [[] for _ in range(len(nums)+1)]
    for n in nums:
        map[n] = map.get(n, 0) + 1
    for key, value in map.items():
        count[value].append(key)
    li = []
    for i in range(len(count)-1, 0, -1):
        for j in count[i]:
            li.append(j)
        if len(li) == k:
            return li

nums = [1,1,2,1,2,4,3,3,3,5,6,2,1,4,2,4,4,4]
k = 3
print(topKFrequent(nums, k))
