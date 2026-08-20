class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify_max(nums)
        k-=1
        while k:
            heapq.heappop_max(nums)
            k-=1
        return nums[0]