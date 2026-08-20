class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, cur, tot):
            if tot == target:
                res.append(cur.copy())
                return
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                if j >= len(candidates) or tot > target:
                    break
                cur.append(candidates[j])
                dfs(j + 1, cur, tot + candidates[j])
                cur.pop()
        dfs(0, [], 0)
        return res