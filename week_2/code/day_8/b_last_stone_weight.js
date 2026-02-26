const MinHeap = require('./min_heap');

/**
 * @param {number[]} stones
 * @return {number}
 */
var lastStoneWeight = function (stones) {
    // We use our MinHeap, but store negative values to simulate a MaxHeap
    const maxHeap = new MinHeap();

    for (let stone of stones) {
        maxHeap.push(-stone);
    }

    while (maxHeap.size() > 1) {
        let stone1 = maxHeap.pop(); // heaviest (most negative)
        let stone2 = maxHeap.pop(); // second heaviest

        if (stone1 !== stone2) {
            maxHeap.push(stone1 - stone2); // e.g., -8 - (-7) = -1
        }
    }

    return maxHeap.size() === 1 ? -maxHeap.peek() : 0;
};

// Example Usage
console.log(lastStoneWeight([2, 7, 4, 1, 8, 1])); // Should output 1
