const MinHeap = require('./min_heap');

var Twitter = function () {
    this.time = 0;
    this.tweets = new Map(); // userId -> Array of { timestamp, tweetId }
    this.followees = new Map(); // userId -> Set of followeeIds
};

/** 
 * @param {number} userId 
 * @param {number} tweetId
 * @return {void}
 */
Twitter.prototype.postTweet = function (userId, tweetId) {
    if (!this.tweets.has(userId)) {
        this.tweets.set(userId, []);
    }
    this.tweets.get(userId).push({ timestamp: this.time, tweetId: tweetId });
    this.time++;
};

/** 
 * @param {number} userId
 * @return {number[]}
 */
Twitter.prototype.getNewsFeed = function (userId) {
    const usersToCheck = new Set(this.followees.get(userId) || []);
    usersToCheck.add(userId);

    // We want a Max-Heap based on timestamp (largest timestamp first)
    // So the comparator should return a value > 0 if b > a => b.timestamp - a.timestamp
    const maxHeap = new MinHeap((a, b) => b.timestamp - a.timestamp);

    for (let uId of usersToCheck) {
        if (this.tweets.has(uId)) {
            const userTweets = this.tweets.get(uId);
            // Get at most 10 recent
            const recent = userTweets.slice(-10);
            for (let t of recent) {
                maxHeap.push(t);
            }
        }
    }

    const feed = [];
    while (maxHeap.size() > 0 && feed.length < 10) {
        feed.push(maxHeap.pop().tweetId);
    }

    return feed;
};

/** 
 * @param {number} followerId 
 * @param {number} followeeId
 * @return {void}
 */
Twitter.prototype.follow = function (followerId, followeeId) {
    if (followerId === followeeId) return;
    if (!this.followees.has(followerId)) {
        this.followees.set(followerId, new Set());
    }
    this.followees.get(followerId).add(followeeId);
};

/** 
 * @param {number} followerId 
 * @param {number} followeeId
 * @return {void}
 */
Twitter.prototype.unfollow = function (followerId, followeeId) {
    if (this.followees.has(followerId)) {
        this.followees.get(followerId).delete(followeeId);
    }
};

// Example Usage
const twitter = new Twitter();
twitter.postTweet(1, 5); // User 1 posts tweet 5
console.log(twitter.getNewsFeed(1)); // return [5]
twitter.follow(1, 2);    // User 1 follows User 2
twitter.postTweet(2, 6); // User 2 posts tweet 6
console.log(twitter.getNewsFeed(1)); // return [6, 5]
twitter.unfollow(1, 2);  // User 1 unfollows User 2
console.log(twitter.getNewsFeed(1)); // return [5]
