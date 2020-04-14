from typing import List


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.follows = {}
        self.news = []
    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if userId not in self.follows:
            self.follows[userId] = []
        tmp = [userId, tweetId]
        if tmp not in self.news:
            self.news = [tmp] + self.news

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        count = 0
        res = []
        if userId in self.follows:
            friends = [userId] + self.follows[userId]
        else:
            return []
        for user, tweet in self.news:
            if count == 10:
                break
            if user in friends:
                res.append(tweet)
                count += 1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId not in self.follows:
            self.follows[followerId] = []
        if followerId != followeeId and followeeId not in self.follows[followerId]:
            self.follows[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId not in self.follows:
             return
        if followerId != followeeId and followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)

twitter = Twitter()
twitter.postTweet(1, 5)
print(twitter.getNewsFeed(1))
twitter.follow(1, 2)
twitter.postTweet(2, 6)
print(twitter.getNewsFeed(1))
# twitter.postTweet(2, 6)
twitter.unfollow(1, 2)
print(twitter.getNewsFeed(1))
