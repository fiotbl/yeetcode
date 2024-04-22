class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        
        self.followMap[userId].add(userId)
        for followee in self.followMap[userId]:
            if followee in self.tweetMap:
                index = len(self.tweetMap[followee]) - 1
                time, tweetId = self.tweetMap[followee][index]
                minHeap.append([time, tweetId, followee, index - 1])
        heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            time, tweetId, followee, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                time, tweetId = self.tweetMap[followee][index]
                heapq.heappush(minHeap, [time, tweetId, followee, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)