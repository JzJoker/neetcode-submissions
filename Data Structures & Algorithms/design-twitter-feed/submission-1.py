class Twitter:

    def __init__(self):
        self.tweets = []
        self.count = 0
        self.users = defaultdict(set) # users, following
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count += 1
        heapq.heappush(self.tweets, ([-self.count, userId, tweetId]))
        
    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        count = 10
        temp = self.tweets.copy()
        while temp and count:
            top = heapq.heappop(temp)
            if top[1] in self.users[userId] or top[1] == userId:
                res.append(top[2])
                count -=1 
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)
