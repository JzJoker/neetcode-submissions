class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        buckets = [[] for i in range(len(nums))]
        for num, count in counts.items():
            buckets[len(nums)-count].append(num)
        res = []
        for bucket in buckets:
            for num in bucket:
                res.append(num)
                if len(res) == k:
                    return res
        

