/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function (candidates, target) {
    const res = [];

    function dfs(i, currentComb, total) {
        // Base Cases
        if (total === target) {
            res.push([...currentComb]);
            return;
        }
        if (i >= candidates.length || total > target) {
            return;
        }

        // Decision 1: Include candidates[i] (and stay at index i to potentially reuse)
        currentComb.push(candidates[i]);
        dfs(i, currentComb, total + candidates[i]);

        // Decision 2: Do NOT include candidates[i] (move on to next index)
        currentComb.pop();
        dfs(i + 1, currentComb, total);
    }

    dfs(0, [], 0);
    return res;
};

// Example Usage
console.log(combinationSum([2, 3, 6, 7], 7)); // [[2, 2, 3], [7]]
console.log(combinationSum([2, 3, 5], 8));    // [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
console.log(combinationSum([2], 1));          // []
