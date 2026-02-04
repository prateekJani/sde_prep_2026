/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
    const charSet = new Set();
    let l = 0;
    let res = 0;

    for (let r = 0; r < s.length; r++) {
        while (charSet.has(s[r])) {
            charSet.delete(s[l]);
            l++;
        }
        charSet.add(s[r]);
        res = Math.max(res, r - l + 1);
    }
    return res;
};

// Test cases
console.log("Test 1 'abcabcbb':", lengthOfLongestSubstring("abcabcbb"), "(Expected: 3)");
console.log("Test 2 'bbbbb':", lengthOfLongestSubstring("bbbbb"), "(Expected: 1)");
console.log("Test 3 'pwwkew':", lengthOfLongestSubstring("pwwkew"), "(Expected: 3)");
