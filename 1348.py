# 1348. Tweet Counts Per Frequency

from collections import defaultdict
from typing import List


class TweetCounts:

    def __init__(self):
        self.tweets = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweets[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int):
        interval = {'minute': 60, 'hour': 3600, 'day': 86400}[freq]
        counts = [0] * ((endTime - startTime) // interval + 1)
        for time in self.tweets[tweetName]:
            if startTime <= time <= endTime:
                counts[(time - startTime) // interval] += 1
        return counts
        


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)

obj = TweetCounts()
obj.recordTweet("tweet3",0)
obj.recordTweet("tweet3",60)
obj.recordTweet("tweet3",10)
print(obj.getTweetCountsPerFrequency("minute","tweet3",0,59))
print(obj.getTweetCountsPerFrequency("minute","tweet3",0,60))
obj.recordTweet("tweet3",120)
print(obj.getTweetCountsPerFrequency("hour","tweet3",0,210))

# ["TweetCounts","recordTweet","recordTweet","recordTweet","getTweetCountsPerFrequency","getTweetCountsPerFrequency","recordTweet","getTweetCountsPerFrequency"]
# [[],["tweet3",0],["tweet3",60],["tweet3",10],["minute","tweet3",0,59],["minute","tweet3",0,60],["tweet3",120],["hour","tweet3",0,210]]

# Output
# [null,null,null,null,[2],[2,1],null,[4]]

# Explanation
# TweetCounts tweetCounts = new TweetCounts();
# tweetCounts.recordTweet("tweet3", 0);                              // New tweet "tweet3" at time 0
# tweetCounts.recordTweet("tweet3", 60);                             // New tweet "tweet3" at time 60
# tweetCounts.recordTweet("tweet3", 10);                             // New tweet "tweet3" at time 10
# tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 59); // return [2]; chunk [0,59] had 2 tweets
# tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 60); // return [2,1]; chunk [0,59] had 2 tweets, chunk [60,60] had 1 tweet
# tweetCounts.recordTweet("tweet3", 120);                            // New tweet "tweet3" at time 120
# tweetCounts.getTweetCountsPerFrequency("hour", "tweet3", 0, 210);  // return [4]; chunk [0,210] had 4 tweets






