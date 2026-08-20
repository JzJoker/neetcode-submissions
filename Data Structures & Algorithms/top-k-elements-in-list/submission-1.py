class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freqs = [[] for i in range(len(nums) + 1)]
        for num in nums:
            count[num] += 1
        for num, cnt in count.items():
            freqs[cnt].append(num)
        res = []
        for i in range(len(freqs) - 1, 0, -1):
            for num in freqs[i]:
                res.append(num)
                if len(res) == k:
                    return res