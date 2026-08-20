class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in range(len(nums1)):
            num = nums1[i]
            found = False
            added = False
            for num2 in nums2:
                if num2 == num:
                    found = True
                if found:
                    if num2 > num:
                        res.append(num2)
                        added = True
                        break
            if not added:
                res.append(-1)
        return res