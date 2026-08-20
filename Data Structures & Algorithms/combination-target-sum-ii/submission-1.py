class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []
        def dfs(i, cur, tot):
            if tot == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or tot > target:
                return
            cur.append(candidates[i])
            dfs(i + 1, cur, tot + candidates[i])
            cur.pop()

            j = i + 1
            while j < n and candidates[j] == candidates[i]:
                j += 1
            dfs(j, cur, tot)
        dfs(0, [], 0)
        return res