class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # jot down indegrees in postreqs
        postreqs = [[] for i in range(numCourses)]
        indegrees = [0] * numCourses
        for post, pre in prerequisites:
            postreqs[pre].append(post)
            indegrees[post] += 1
        
        finished = 0
        # queue all indegree 0 courses
        q = deque()
        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                q.append(i)
        
        while q:
            course = q.popleft()
            finished += 1
            posts = postreqs[course]
            for post in posts:
                indegrees[post] -= 1
                if indegrees[post] == 0:
                    q.append(post)
        return finished == numCourses