def insert(intervals, newInterval):
    res = []

    for i, intvl in enumerate(intervals):
        if intvl[0] > newInterval[1]:
            res.append(newInterval)
            return res + intervals[i:]
        elif intvl[1] < newInterval[0]:
            res.append(intvl)
        else:
            newInterval = [min(intvl[0], newInterval[0]), 
                           max(intvl[1], newInterval[1])]
    
    res.append(newInterval)
    return res

print(insert([[1, 3], [6, 8]], [2, 5]))