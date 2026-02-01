/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
    const map = new Map();

    for (let i = 0; i < nums.length; i++) {
        const diff = target - nums[i];
        if (map.has(diff)) {
            return [map.get(diff), i];
        }
        map.set(nums[i], i);
    }
    return [];
};


// Test cases
console.log("Test 1 [2,7,11,15], 9:", twoSum([2, 7, 11, 15], 9), "(Expected: [0, 1])");
console.log("Test 2 [3,2,4], 6:", twoSum([3, 2, 4], 6), "(Expected: [1, 2])");
console.log("Test 3 [3,3], 6:", twoSum([3, 3], 6), "(Expected: [0, 1])");
