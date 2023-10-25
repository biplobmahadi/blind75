def combinationSum(candidates, target):
    res = []
    def solve(arr, i):
        total = 0
        for n in arr:
            total+=n
        if total == target:
            res.append(arr.copy())
            return
        if total > target: return
        for j in range(i, len(candidates)):
            arr.append(candidates[j])
            solve(arr, j)
            arr.pop()
    solve([], 0)
    return res

print(combinationSum([2, 5, 3], 8))
