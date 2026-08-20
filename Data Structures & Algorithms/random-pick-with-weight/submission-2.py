class Solution:

    def __init__(self, w: List[int]):
        self.nums = []
        for i in range(len(w)):
            num = w[i]
            for n in range(num):
                self.nums.append([num, i])

    def pickIndex(self) -> int:
        return random.choice(self.nums)[1]


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()