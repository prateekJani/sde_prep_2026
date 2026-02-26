import heapq
from collections import defaultdict

class Twitter:
    def __init__(self):
        # Global counter to act as a timestamp (lower means older)
        self.time = 0
        self.tweets = defaultdict(list) # userId -> list of [timestamp, tweetId]
        self.followees = defaultdict(set) # userId -> set of followeeIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.time, tweetId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        # A user automatically follows themselves for the news feed
        users_to_check = self.followees[userId].copy()
        users_to_check.add(userId)
        
        # Max-heap to get the 10 most recent tweets
        # (Stored as max-heap using -timestamp)
        max_heap = []
        for uId in users_to_check:
            # Add up to the 10 most recent tweets of each followed user
            user_tweets = self.tweets[uId][-10:]
            for timestamp, tId in user_tweets:
                max_heap.append([-timestamp, tId])
        
        heapq.heapify(max_heap)
        
        # Extract at most 10 most recent tweets
        feed = []
        while max_heap and len(feed) < 10:
            feed.append(heapq.heappop(max_heap)[1])
            
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followees[followerId]:
            self.followees[followerId].remove(followeeId)

# Example Usage
if __name__ == "__main__":
    twitter = Twitter()
    twitter.postTweet(1, 5)  # User 1 posts tweet 5
    print(twitter.getNewsFeed(1))  # return [5]
    twitter.follow(1, 2)     # User 1 follows User 2
    twitter.postTweet(2, 6)  # User 2 posts tweet 6
    print(twitter.getNewsFeed(1))  # return [6, 5]
    twitter.unfollow(1, 2)   # User 1 unfollows User 2
    print(twitter.getNewsFeed(1))  # return [5]
