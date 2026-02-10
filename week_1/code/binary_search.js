/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function (nums, target) {
    let l = 0;
    let r = nums.length - 1;

    while (l <= r) {
        const mid = Math.floor((l + r) / 2);
        if (nums[mid] > target) {
            r = mid - 1;
        } else if (nums[mid] < target) {
            l = mid + 1;
        } else {
            return mid;
        }
    }
    return -1;
};

// Test cases
console.log("Test 1 [-1,0,3,5,9,12], 9:", search([-1, 0, 3, 5, 9, 12], 9), "(Expected: 4)");
console.log("Test 2 [-1,0,3,5,9,12], 2:", search([-1, 0, 3, 5, 9, 12], 2), "(Expected: -1)");
