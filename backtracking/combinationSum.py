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

def combinationSum2(candidates, target):
    res = []
    def solve(i, total, list):
        if total == target:
            res.append(list.copy())
            return
        if i == len(candidates) or total > target:
            return
        list.append(candidates[i])
        solve(i, total+candidates[i], list)
        list.pop()
        solve(i+1, total, list)
    solve(0, 0, [])
    return res

print(combinationSum2([2, 5, 3], 8))