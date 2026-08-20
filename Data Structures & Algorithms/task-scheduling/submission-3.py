class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        maxHeap = [-count for count in counts.values()]
        heapq.heapify(maxHeap)

        q = deque()
        time = 0
        while maxHeap or q:
            print(maxHeap)
            print(q)
            time += 1
            if not maxHeap:
                time = q[0][1]
            else:
                count = heapq.heappop(maxHeap) + 1
                if count:
                    q.append([count, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time


