const MinHeap = require('./min_heap');

/**
 * @param {number[][]} points
 * @param {number} k
 * @return {number[][]}
 */
var kClosest = function (points, k) {
    // We want a Max-Heap based on distance to keep the K closest.
    // So the comparator should return a > b, simulating Max-Heap.
    // Comparator for MinHeap: (a, b) => a - b
    // Comparator for MaxHeap: (a, b) => b - a

    const maxHeap = new MinHeap((a, b) => {
        const distA = a[0] * a[0] + a[1] * a[1];
        const distB = b[0] * b[0] + b[1] * b[1];
        return distB - distA; // This reverse order turns MinHeap logic into MaxHeap
    });

    for (let point of points) {
        maxHeap.push(point);
        if (maxHeap.size() > k) {
            maxHeap.pop(); // Remove the farthest point
        }
    }

    // Extract all points from heap
    const result = [];
    while (maxHeap.size() > 0) {
        result.push(maxHeap.pop());
    }

    return result;
};

// Example Usage
console.log(kClosest([[1, 3], [-2, 2]], 1)); // [[-2, 2]]
console.log(kClosest([[3, 3], [5, -1], [-2, 4]], 2)); // [[3, 3], [-2, 4]]
