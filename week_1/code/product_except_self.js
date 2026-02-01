/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function (nums) {
    const n = nums.length;
    const res = new Array(n).fill(1);

    let prefix = 1;
    for (let i = 0; i < n; i++) {
        res[i] = prefix;
        prefix *= nums[i];
    }

    let postfix = 1;
    for (let i = n - 1; i >= 0; i--) {
        res[i] *= postfix;
        postfix *= nums[i];
    }

    return res;
};

// Test cases
console.log("Test 1 [1,2,3,4]:", productExceptSelf([1, 2, 3, 4]), "(Expected: [24,12,8,6])");
console.log("Test 2 [-1,1,0,-3,3]:", productExceptSelf([-1, 1, 0, -3, 3]), "(Expected: [0,0,9,0,0])");
