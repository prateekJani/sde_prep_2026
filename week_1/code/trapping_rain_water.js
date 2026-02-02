/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function (height) {
    let l = 0;
    let r = height.length - 1;
    let leftMax = height[l];
    let rightMax = height[r];
    let res = 0;

    while (l < r) {
        if (leftMax < rightMax) {
            l++;
            leftMax = Math.max(leftMax, height[l]);
            res += leftMax - height[l];
        } else {
            r--;
            rightMax = Math.max(rightMax, height[r]);
            res += rightMax - height[r];
        }
    }
    return res;
};

// Test cases
console.log("Test 1 [0,1,0,2,1,0,1,3,2,1,2,1]:", trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), "(Expected: 6)");
console.log("Test 2 [4,2,0,3,2,5]:", trap([4, 2, 0, 3, 2, 5]), "(Expected: 9)");
