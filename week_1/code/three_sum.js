/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function (nums) {
    const res = [];
    nums.sort((a, b) => a - b);

    for (let i = 0; i < nums.length; i++) {
        // Skip positive integers
        if (nums[i] > 0) break;

        // Skip duplicates for 'a'
        if (i > 0 && nums[i] === nums[i - 1]) continue;

        let l = i + 1;
        let r = nums.length - 1;

        while (l < r) {
            const sum = nums[i] + nums[l] + nums[r];
            if (sum > 0) {
                r--;
            } else if (sum < 0) {
                l++;
            } else {
                res.push([nums[i], nums[l], nums[r]]);
                l++;
                r--;
                // Skip duplicates for 'l'
                while (l < r && nums[l] === nums[l - 1]) {
                    l++;
                }
            }
        }
    }
    return res;
};

// Test cases
console.log("Test 1 [-1,0,1,2,-1,-4]:", threeSum([-1, 0, 1, 2, -1, -4]), "(Expected: [[-1,-1,2],[-1,0,1]])");
console.log("Test 2 [0,1,1]:", threeSum([0, 1, 1]), "(Expected: [])");
console.log("Test 3 [0,0,0]:", threeSum([0, 0, 0]), "(Expected: [[0,0,0]])");
