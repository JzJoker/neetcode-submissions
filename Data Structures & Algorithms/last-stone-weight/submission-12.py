class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            x, y = heapq.heappop(maxHeap), heapq.heappop(maxHeap)
            if x < y:
                heapq.heappush(maxHeap, x-y)
        if maxHeap:
            return abs(maxHeap[0])
        else:
            return 0