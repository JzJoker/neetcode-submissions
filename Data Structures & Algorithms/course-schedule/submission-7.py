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
            for prereq in prereqs[course]:
                if not dfs(prereq):
                    return False
            visiting.remove(course)
            prereqs[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
        

