/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
    if (s.length !== t.length) return false;

    const map = {};

    for (let char of s) {
        map[char] = (map[char] || 0) + 1;
    }

    for (let char of t) {
        if (!map[char]) return false;
        map[char]--;
    }

    return true;
};

// Test cases
console.log("Test 1 (anagram, nagaram):", isAnagram("anagram", "nagaram"), "(Expected: true)");
console.log("Test 2 (rat, car):", isAnagram("rat", "car"), "(Expected: false)");
