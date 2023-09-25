# 355. Design Twitter
# https://leetcode.com/problems/design-twitter/


import collections
import itertools
import heapq
from typing import List
from collections import deque


class Twitter:

    def __init__(self):

        self.timer = itertools.count(step=-1)
        self.tweets = collections.defaultdict(deque)
        self.folowees = collections.defaultdict(set)


    def postTweet(self, userId: int, tweetId: int) -> None:
        
        self.tweets[userId].appendleft((next(self.timer), tweetId))
        
        if len(self.tweets[userId]) > 10:
            self.tweets[userId].pop()


    def getNewsFeed(self, userId: int) -> List[int]:
        
        tweets = list(heapq.merge(*(self.tweets[followee] for followee in self.folowees[userId] | {userId})))
        return [tweetId for _, tweetId in tweets[:10]]


    def follow(self, followerId: int, followeeId: int) -> None:
        self.folowees[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.folowees[followerId].discard(followeeId)
        


obj = Twitter()
obj.postTweet(1, 5)
obj.getNewsFeed(1)
obj.follow(1, 2)
obj.postTweet(2, 6)
print(obj.getNewsFeed(1))
obj.unfollow(1, 2)
print(obj.getNewsFeed(1))



# Output: [null, null, [5], null, null, [6, 5], null, [5]]

# Explanation
# Twitter twitter = new Twitter();
# twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
# twitter.follow(1, 2);    // User 1 follows user 2.
# twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
# twitter.unfollow(1, 2);  // User 1 unfollows user 2.
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.




