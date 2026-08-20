class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-stone for stone in stones]
        heapq.heapify(maxheap)
        while len(maxheap) > 1:
            x, y = heapq.heappop(maxheap), heapq.heappop(maxheap)
            if x < y:
                heapq.heappush(maxheap, x - y)
        if maxheap:
            return abs(maxheap[0])
        else:
            return 0