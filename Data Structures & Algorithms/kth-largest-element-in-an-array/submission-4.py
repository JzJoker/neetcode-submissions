class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = nums
        heapq.heapify(maxHeap)
        return heapq.nlargest(k, maxHeap)[-1]