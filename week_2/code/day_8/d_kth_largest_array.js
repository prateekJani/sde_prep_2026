const MinHeap = require('./min_heap');

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findKthLargest = function (nums, k) {
    // Min-heap of size K
    const minHeap = new MinHeap((a, b) => a - b);

    for (let i = 0; i < k; i++) {
        minHeap.push(nums[i]);
    }

    for (let i = k; i < nums.length; i++) {
        if (nums[i] > minHeap.peek()) {
            minHeap.pop(); // remove smallest
            minHeap.push(nums[i]); // add larger
        }
    }

    return minHeap.peek();
};

// Example Usage
console.log(findKthLargest([3, 2, 1, 5, 6, 4], 2)); // 5
console.log(findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)); // 4
