/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function (n) {
    const stack = [];
    const res = [];

    function backtrack(openN, closedN) {
        if (openN === n && closedN === n) {
            res.push(stack.join(''));
            return;
        }

        if (openN < n) {
            stack.push('(');
            backtrack(openN + 1, closedN);
            stack.pop();
        }

        if (closedN < openN) {
            stack.push(')');
            backtrack(openN, closedN + 1);
            stack.pop();
        }
    }

    backtrack(0, 0);
    return res;
};

// Test cases
console.log("Test 1 n=3:", generateParenthesis(3));
console.log("Test 2 n=1:", generateParenthesis(1));
