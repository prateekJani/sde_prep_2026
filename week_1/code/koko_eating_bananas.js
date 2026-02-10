/**
 * @param {number[]} piles
 * @param {number} h
 * @return {number}
 */
var minEatingSpeed = function (piles, h) {
    let l = 1;
    let r = Math.max(...piles);
    let res = r;

    while (l <= r) {
        const k = Math.floor((l + r) / 2);
        let hours = 0;
        for (const p of piles) {
            hours += Math.ceil(p / k);
        }

        if (hours <= h) {
            res = Math.min(res, k);
            r = k - 1;
        } else {
            l = k + 1;
        }
    }
    return res;
};

// Test cases
console.log("Test 1 [3,6,7,11], h=8:", minEatingSpeed([3, 6, 7, 11], 8), "(Expected: 4)");
console.log("Test 2 [30,11,23,4,20], h=5:", minEatingSpeed([30, 11, 23, 4, 20], 5), "(Expected: 30)");
console.log("Test 3 [30,11,23,4,20], h=6:", minEatingSpeed([30, 11, 23, 4, 20], 6), "(Expected: 23)");
