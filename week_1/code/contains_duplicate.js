/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
    // TODO: Implement this

    const set = new Set(nums);
    return set.size !== nums.length;
};

// Test cases
console.log("Test 1 [1,2,3,1]:", containsDuplicate([1, 2, 3, 1]), "(Expected: true)");
console.log("Test 2 [1,2,3,4]:", containsDuplicate([1, 2, 3, 4]), "(Expected: false)");
console.log("Test 3 [1,1,1,3,3,4,3,2,4,2]:", containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), "(Expected: true)");
