
var MinStack = function () {
    this.stack = [];
    this.minStack = [];
};

/** 
 * @param {number} val
 * @return {void}
 */
MinStack.prototype.push = function (val) {
    this.stack.push(val);
    if (this.minStack.length === 0) {
        this.minStack.push(val);
    } else {
        this.minStack.push(Math.min(val, this.minStack[this.minStack.length - 1]));
    }
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function () {
    this.stack.pop();
    this.minStack.pop();
};

/**
 * @return {number}
 */
MinStack.prototype.top = function () {
    return this.stack[this.stack.length - 1];
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function () {
    return this.minStack[this.minStack.length - 1];
};

// Test cases
var obj = new MinStack();
obj.push(-2);
obj.push(0);
obj.push(-3);
console.log("getMin:", obj.getMin(), "(Expected: -3)");
obj.pop();
console.log("top:", obj.top(), "(Expected: 0)");
console.log("getMin:", obj.getMin(), "(Expected: -2)");
