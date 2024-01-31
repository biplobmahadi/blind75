def erase(intervals):
    intervals.sort(key= lambda pair: pair[0])
    count = 0
    running = intervals[0]
    for curr in intervals[1:]:
        if running[1] > curr[0]:
            count+=1
            if running[1] > curr[1]:
                running = curr
        else:
            running = curr
    return count

print(erase([[1,2],[2,3],[3,4],[1,3]]))
