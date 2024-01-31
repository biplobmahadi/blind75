def merge(intervals):
    intervals.sort(key= lambda pair: pair[0])
    res = []
    running = intervals[0]
    for i in range(1, len(intervals)):
        curr = intervals[i]
        if running[1] >= curr[0]:
            running = [min(running[0], curr[0]), 
                       max(running[1], curr[1])]
        else:
            res.append(running)
            running = curr
    res.append(running)
    return res

print(merge([[1,4],[0,0]]))
