/**
 * @param {string[]} tokens
 * @return {number}
 */
var evalRPN = function (tokens) {
    let stack = [];

    for (const t of tokens) {
        if (t === "+") {
            stack.push(stack.pop() + stack.pop());
        } else if (t === "-") {
            let a = stack.pop();
            let b = stack.pop();
            stack.push(b - a);
        } else if (t === "*") {
            stack.push(stack.pop() * stack.pop());
        } else if (t === "/") {
            let a = stack.pop();
            let b = stack.pop();
            stack.push(Math.trunc(b / a));
        } else {
            stack.push(Number(t));
        }
    }
    return stack[0];
};

// Test cases
console.log("Test 1 ['2','1','+','3','*']:", evalRPN(["2", "1", "+", "3", "*"]), "(Expected: 9)");
console.log("Test 2 ['4','13','5','/','+']:", evalRPN(["4", "13", "5", "/", "+"]), "(Expected: 6)");
console.log("Test 3 ['10','6','9','3','+','-11','*','/','*','17','+','5','+']:", evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]), "(Expected: 22)");
