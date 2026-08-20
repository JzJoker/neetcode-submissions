class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # jot down indegree and postreq of each class
        indegree = [0] * numCourses
        postreq = [[] for i in range(numCourses)]
        finished = 0
        for pair in prerequisites:
            indegree[pair[0]] += 1
            postreq[pair[1]].append(pair[0])

        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        print(postreq)
        print(q)
        while q:
            course = q.popleft()
            finished += 1
            dependents = postreq[course]
            print(dependents)
            for course in dependents:
                indegree[course] -= 1
                if indegree[course] == 0:
                    q.append(course)
        print(finished)
        print(indegree)
        return finished == numCourses