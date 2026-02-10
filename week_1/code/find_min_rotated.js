/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function (nums) {
    let res = nums[0];
    let l = 0;
    let r = nums.length - 1;

    while (l <= r) {
        if (nums[l] < nums[r]) {
            res = Math.min(res, nums[l]);
            break;
        }

        const mid = Math.floor((l + r) / 2);
        res = Math.min(res, nums[mid]);

        if (nums[mid] >= nums[l]) {
            l = mid + 1;
        } else {
            r = mid - 1;
        }
    }
    return res;
};

// Test cases
console.log("Test 1 [3,4,5,1,2]:", findMin([3, 4, 5, 1, 2]), "(Expected: 1)");
console.log("Test 2 [4,5,6,7,0,1,2]:", findMin([4, 5, 6, 7, 0, 1, 2]), "(Expected: 0)");
console.log("Test 3 [11,13,15,17]:", findMin([11, 13, 15, 17]), "(Expected: 11)");
