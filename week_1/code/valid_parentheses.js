/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
    const stack = [];
    const closeToOpen = { ')': '(', '}': '{', ']': '[' };

    for (let c of s) {
        if (closeToOpen[c]) {
            if (stack.length > 0 && stack[stack.length - 1] === closeToOpen[c]) {
                stack.pop();
            } else {
                return false;
            }
        } else {
            stack.push(c);
        }
    }
    return stack.length === 0;
};

// Test cases
console.log("Test 1 '()':", isValid("()"), "(Expected: true)");
console.log("Test 2 '()[]{}':", isValid("()[]{}"), "(Expected: true)");
console.log("Test 3 '(]':", isValid("(]"), "(Expected: false)");
console.log("Test 4 '([])':", isValid("([])"), "(Expected: true)");
