class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count tasks
        counts = Counter(tasks)
        # Create max heap
        maxHeap = [-c for c in counts.values()]
        heapq.heapify(maxHeap)

        q = deque()  # [remaining(neg), availableAt]
        time = 0
        while maxHeap or q:
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
