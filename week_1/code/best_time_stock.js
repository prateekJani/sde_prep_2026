/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
    // TODO: Implement using Sliding Window logic

    let l = 0;
    let r = 1;
    let profit = 0;

    while (r < prices.length) {
        if (prices[l] < prices[r]) {
            profit = Math.max(prices[r] - prices[l], profit);
        } else {
            l = r;
        }
        r++;
    }

    return profit;

};

// Test cases
console.log("Test 1 [7,1,5,3,6,4]:", maxProfit([7, 1, 5, 3, 6, 4]), "(Expected: 5)");
console.log("Test 2 [7,6,4,3,1]:", maxProfit([7, 6, 4, 3, 1]), "(Expected: 0)");
