class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

def meetingRoom2(intervals):
    start = sorted([i.start for i in intervals])
    end = sorted([i.end for i in intervals])
    s, e = 0, 0
    res, count = 0, 0
    while s < len(start):
        if start[s] < end[e]:
            count+=1
            s+=1
        else:
            count-=1
            e+=1
        res = max(res, count)
    return res

print(meetingRoom2([Interval(0,50),Interval(10,60),Interval(60,110),Interval(70,120),Interval(20,70),Interval(30,80),Interval(40,90),Interval(50,100),Interval(80,130),Interval(90,140),Interval(100,150)]))
