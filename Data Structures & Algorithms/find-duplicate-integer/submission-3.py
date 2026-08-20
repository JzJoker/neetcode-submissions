class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break
        slow1 = 0
        while True:
            slow1 = nums[slow1]
            slow = nums[slow]
            if slow1 == slow:
                return slow1