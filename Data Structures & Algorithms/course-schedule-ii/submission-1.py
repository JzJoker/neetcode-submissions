class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # jot down indegree and postreqs
        postreq = [[] for i in range(numCourses)]
        indegree = [0] * numCourses
        for post, pre in prerequisites:
            postreq[pre].append(post)
            indegree[post] += 1

        order = []
        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            course = q.popleft()
            posts = postreq[course]
            order.append(course)
            for post in posts:
                indegree[post] -= 1
                if indegree[post] == 0:
                    q.append(post)
        return [] if len(order) != numCourses else order