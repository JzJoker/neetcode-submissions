class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int) # num -> count
        for num in nums:
            count[num] += 1
        # bucket
        bucket = [[] for i in range(len(nums) + 1)]
        print(bucket)
        for num, count in count.items():
            bucket[count].append(num)
        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res

