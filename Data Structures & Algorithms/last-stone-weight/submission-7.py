class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minHeap = [-s for s in stones]
        heapq.heapify(minHeap)

        while len(minHeap) > 1:
            x, y = heapq.heappop(minHeap), heapq.heappop(minHeap)
            if x < y:
                heapq.heappush(minHeap, x - y)
        if minHeap:
            return abs(minHeap[0])
        else:
            return 0