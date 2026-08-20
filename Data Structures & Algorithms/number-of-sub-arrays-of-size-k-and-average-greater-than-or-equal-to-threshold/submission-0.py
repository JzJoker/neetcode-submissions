class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        startWindow = arr[0:k]
        tot = 0
        for num in startWindow:
            tot += num
        startAvg = tot // k
        res = 0
        if startAvg >= threshold:
            res += 1
        for i in range(k, len(arr)):
            tot -= arr[i - k]
            tot += arr[i]
            startAvg = tot // k
            if startAvg >= threshold:
                res += 1
        return res