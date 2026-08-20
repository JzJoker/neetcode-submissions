class MedianFinder:

    def __init__(self):
        self.lower = []
        self.higher = []
    def addNum(self, num: int) -> None:
        heapq.heappush(self.higher, num)
        heapq.heappush(self.lower, - self.higher[0])
        heapq.heappop(self.higher)

        if len(self.higher) < len(self.lower):
            x = heapq.heappop(self.lower)
            heapq.heappush(self.higher, -x)
    def findMedian(self) -> float:
        if len(self.higher) == len(self.lower):
            return (self.higher[0] - self.lower[0]) / 2
        else:
            return self.higher[0]