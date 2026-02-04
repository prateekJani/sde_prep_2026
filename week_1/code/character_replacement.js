/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var characterReplacement = function (s, k) {
    const count = {};
    let res = 0;
    let l = 0;
    let maxf = 0;

    for (let r = 0; r < s.length; r++) {
        count[s[r]] = (count[s[r]] || 0) + 1;
        maxf = Math.max(maxf, count[s[r]]);

        while ((r - l + 1) - maxf > k) {
            count[s[l]] -= 1;
            l++;
        }
        res = Math.max(res, r - l + 1);
    }
    return res;
};

// Test cases
console.log("Test 1 'ABAB', k=2:", characterReplacement("ABAB", 2), "(Expected: 4)");
console.log("Test 2 'AABABBA', k=1:", characterReplacement("AABABBA", 1), "(Expected: 4)");
