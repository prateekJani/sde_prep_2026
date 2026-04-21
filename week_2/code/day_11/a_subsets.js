/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function (nums) {
    const res = [];
    const subset = [];

    function dfs(i) {
        if (i >= nums.length) {
            // Need a shallow copy because the 'subset' array reference is reused
            res.push([...subset]);
            return;
        }

        // Decision to INCLUDE the number
        subset.push(nums[i]);
        dfs(i + 1);

        // Decision to NOT INCLUDE the number
        subset.pop();
        dfs(i + 1);
    }

    dfs(0);
    return res;
};

// Example Usage
console.log(subsets([1, 2, 3]));
// [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]

console.log(subsets([0]));
// [[0], []]
