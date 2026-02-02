/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
    let left = 0;
    let right = s.length - 1;

    while (left < right) {
        if (!/^[a-z0-9]$/i.test(s[left])) {
            left++;
            continue;
        }
        if (!/^[a-z0-9]$/i.test(s[right])) {
            right--;
            continue;
        }
        if (s[left].toLowerCase() !== s[right].toLowerCase()) {
            return false;
        }
        left++;
        right--;
    }
    return true;
};

// Test cases
console.log("Test 1 'A man, a plan, a canal: Panama':", isPalindrome("A man, a plan, a canal: Panama"), "(Expected: true)");
console.log("Test 2 'race a car':", isPalindrome("race a car"), "(Expected: false)");
console.log("Test 3 ' ':", isPalindrome(" "), "(Expected: true)");
