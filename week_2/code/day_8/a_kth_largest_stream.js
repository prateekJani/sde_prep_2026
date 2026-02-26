const MinHeap = require('./min_heap');

class KthLargest {
    /**
     * @param {number} k
     * @param {number[]} nums
     */
    constructor(k, nums) {
        this.k = k;
        this.heap = new MinHeap();
        for (let num of nums) {
            this.add(num);
        }
    }

    /** 
     * @param {number} val
     * @return {number}
     */
    add(val) {
        this.heap.push(val);
        if (this.heap.size() > this.k) {
            this.heap.pop();
        }
        return this.heap.peek();
    }
}

// Example Usage
const kthLargest = new KthLargest(3, [4, 5, 8, 2]);
console.log(kthLargest.add(3)); // return 4
console.log(kthLargest.add(5)); // return 5
console.log(kthLargest.add(10)); // return 5
console.log(kthLargest.add(9)); // return 8
console.log(kthLargest.add(4)); // return 8
