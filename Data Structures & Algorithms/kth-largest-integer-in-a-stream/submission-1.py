class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # turn nums into heap
        self.k, self.nums = k, nums
        heapq.heapify(self.nums)
        # pop from top until length is equal to k
        while len(self.nums) > k:
            heapq.heappop(self.nums)
    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]