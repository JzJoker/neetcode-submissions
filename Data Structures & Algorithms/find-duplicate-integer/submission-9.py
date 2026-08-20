class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = slow = 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
        slow1 = 0
        while True:
            slow = nums[slow]
            slow1 = nums[slow1]
            if slow == slow1:
                return slow1
        