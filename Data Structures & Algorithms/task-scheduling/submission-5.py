class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = list(Counter(tasks).values())
        counts = [-count for count in counts]
        heapq.heapify(counts)
        q = deque()
        time = 0
        while counts or q:
            time += 1
            if not counts:
                time = q[0][1]
            else:
                count = heapq.heappop(counts) +  1
                if count:
                    q.append([count, time + n])
            if q and q[0][1] == time:
                heapq.heappush(counts, (q.popleft()[0]))
        return time