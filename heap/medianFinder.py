from heapq import heappush, heappop

class Median:
    def __init__(self) -> None:
        self.small = []
        self.large = []
    
    def insert(self, n):
        heappush(self.small, -1 * n)
        if self.large:
            if self.large[0] < -1 * self.small[0]:
                heappush(self.large, -1 * heappop(self.small))

        if len(self.large)+1 < len(self.small):
            p = heappop(self.small)
            heappush(self.large, -1 * p)

        if len(self.large) > len(self.small)+1:
            p = heappop(self.large)
            heappush(self.small, -1 * p)
    
    def getMedian(self):
        if not self.large and not self.small:
            return None
        if len(self.large) > len(self.small):
            return self.large[0]
        elif len(self.large) < len(self.small):
            return self.small[0] * -1
        return (self.large[0] + (self.small[0] * -1)) / 2

m = Median()
m.insert(40)
m.insert(30)
m.insert(20)
m.insert(10)
m.insert(5)
print(m.getMedian())