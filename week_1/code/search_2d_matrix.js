/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function (matrix, target) {
    const ROWS = matrix.length;
    const COLS = matrix[0].length;
    let l = 0;
    let r = ROWS * COLS - 1;

    while (l <= r) {
        let mid = Math.floor((l + r) / 2);
        let midVal = matrix[Math.floor(mid / COLS)][mid % COLS];

        if (midVal > target) {
            r = mid - 1;
        } else if (midVal < target) {
            l = mid + 1;
        } else {
            return true;
        }
    }
    return false;
};

// Test cases
console.log("Test 1 Found:", searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3), "(Expected: true)");
console.log("Test 2 Not Found:", searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13), "(Expected: false)");
