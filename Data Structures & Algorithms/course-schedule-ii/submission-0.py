class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqs = defaultdict(list)
        for prereq in prerequisites:
            prereqs[prereq[0]].append(prereq[1])
        
        res = []
        visiting, visited = set(), set()
        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True
            visiting.add(course)
            for pre in prereqs[course]:
                if not dfs(pre):
                    return False
            visiting.remove(course)
            visited.add(course)
            res.append(course)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        return res