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
        if (nums[mid] === target) {
            return mid;
        }

        // Left half is sorted
        if (nums[l] <= nums[mid]) {
            if (nums[l] <= target && target < nums[mid]) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        // Right half is sorted
        else {
            if (nums[mid] < target && target <= nums[r]) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
    }
    return -1;
};

// Test cases
console.log("Test 1 [4,5,6,7,0,1,2], 0:", search([4, 5, 6, 7, 0, 1, 2], 0), "(Expected: 4)");
console.log("Test 2 [4,5,6,7,0,1,2], 3:", search([4, 5, 6, 7, 0, 1, 2], 3), "(Expected: -1)");
console.log("Test 3 [1], 0:", search([1], 0), "(Expected: -1)");
