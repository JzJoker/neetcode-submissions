class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = defaultdict(int)
        prevMax = float('-inf')
        count = 0
        l = 0
        res = []
        for right in nums:
            window[right] += 1
            count += 1
            prevMax = max(right, prevMax)
            if count == k:
                res.append(prevMax)
                left = nums[l]
                window[left] -= 1
                if window[left] == 0:
                    del window[left]
                    if left == prevMax: 
                        if window:
                            prevMax = max(list(window.keys()))
                        else:
                            prevMax = float('-inf')
                l += 1
                count -= 1
        return res