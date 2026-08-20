class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elementCounts = defaultdict(int) # num -> count
        for num in nums:
            elementCounts[num]+=1
        
        countElements = defaultdict(list) # count -> nums
        for num, count in elementCounts.items():
            countElements[count].append(num)
        counts = sorted(countElements.keys(), reverse=True)

        res = [] # nums sorted by frequency
        for count in counts:
            res += countElements[count]
        return res[:k]
