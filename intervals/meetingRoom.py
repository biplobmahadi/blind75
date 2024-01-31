def meetingRoom(intervals):
    intervals.sort(key=lambda pair: pair.start)
    runningEnd = intervals[0].end
    for inte in intervals[1:]:
        if runningEnd > inte.start:
            return False
        else:
            runningEnd = inte.end
    return True

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

one = Interval(0,8)
two = Interval(5, 10)
print(meetingRoom([one, two]))
