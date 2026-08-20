class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = defaultdict(list)
        for prereq in prerequisites:
            prereqs[prereq[1]].append(prereq[0])
        
        visiting = set()

        def dfs(course):
            if course in visiting:
                return False
            if prereqs[course] == []:
                return True
            
            visiting.add(course)
            for pre in prereqs[course]:
                if not dfs(pre):
                    return False
            visiting.remove(course)
            prereqs[course] = []
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True