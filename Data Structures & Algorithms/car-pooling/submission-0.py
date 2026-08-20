class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        cur = 0
        stops = []
        for trip in trips:
            while len(stops) < trip[2]:
                stops.append(0)
            for i in range(trip[1], trip[2]):
                stops[i] += trip[0]
        for stop in stops:
            print(stop)
            if stop > capacity:
                return False
        return True