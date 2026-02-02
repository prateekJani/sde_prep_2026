/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function (height) {
    let left = 0;
    let right = height.length - 1;
    let maxArea = 0;

    while (left < right) {
        const width = right - left;
        const currentArea = width * Math.min(height[left], height[right]);
        maxArea = Math.max(maxArea, currentArea);

        if (height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
    }
    return maxArea;
};

// Test cases
console.log("Test 1 [1,8,6,2,5,4,8,3,7]:", maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]), "(Expected: 49)");
console.log("Test 2 [1,1]:", maxArea([1, 1]), "(Expected: 1)");
