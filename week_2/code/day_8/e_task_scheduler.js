const MinHeap = require('./min_heap');

/**
 * @param {character[]} tasks
 * @param {number} n
 * @return {number}
 */
var leastInterval = function (tasks, n) {
    // Count task frequencies
    const count = new Map();
    for (let task of tasks) {
        count.set(task, (count.get(task) || 0) + 1);
    }

    // Max-heap to store frequencies
    const maxHeap = new MinHeap((a, b) => b - a);

    for (let val of count.values()) {
        maxHeap.push(val);
    }

    let time = 0;
    // Queue to store the cooldown: { remainingCount, unlockTime }
    const q = [];

    while (maxHeap.size() > 0 || q.length > 0) {
        time++;

        if (maxHeap.size() > 0) {
            let cnt = maxHeap.pop(); // Most frequent remaining
            cnt--; // Process one instance

            if (cnt > 0) {
                // Add to cooldown queue
                q.push({ remainingCount: cnt, unlockTime: time + n });
            }
        }

        // Check if any task in cooldown is ready
        if (q.length > 0 && q[0].unlockTime === time) {
            maxHeap.push(q.shift().remainingCount);
        }
    }

    return time;
};

// Example Usage
console.log(leastInterval(["A", "A", "A", "B", "B", "B"], 2)); // 8
console.log(leastInterval(["A", "C", "A", "B", "D", "B"], 1)); // 6
console.log(leastInterval(["A", "A", "A", "B", "B", "B"], 3)); // 10
