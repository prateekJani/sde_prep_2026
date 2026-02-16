/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val)
    this.left = (left === undefined ? null : left)
    this.right = (right === undefined ? null : right)
}

/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */
var invertTree = function (root) {
    if (!root) return null;

    let temp = root.left;
    root.left = invertTree(root.right);
    root.right = invertTree(temp);

    return root;
};

// Helper to print tree (Level Order)
function printTree(root) {
    if (!root) {
        console.log("[]");
        return;
    }
    let queue = [root];
    let res = [];
    while (queue.length > 0) {
        let node = queue.shift();
        if (node) {
            res.push(node.val);
            queue.push(node.left);
            queue.push(node.right);
        } else {
            res.push("null");
        }
    }
    // Clean up trailing nulls
    while (res.length > 0 && res[res.length - 1] === "null") {
        res.pop();
    }
    console.log("[" + res.join(",") + "]");
}

// Helper to build tree from array
function buildTree(arr) {
    if (!arr.length) return null;
    let root = new TreeNode(arr[0]);
    let queue = [root];
    let i = 1;
    while (queue.length > 0 && i < arr.length) {
        let node = queue.shift();
        if (i < arr.length && arr[i] !== null) {
            node.left = new TreeNode(arr[i]);
            queue.push(node.left);
        }
        i++;
        if (i < arr.length && arr[i] !== null) {
            node.right = new TreeNode(arr[i]);
            queue.push(node.right);
        }
        i++;
    }
    return root;
}

// Test cases
// Test 1: [4,2,7,1,3,6,9]
let root1 = buildTree([4, 2, 7, 1, 3, 6, 9]);
console.log("Original 1:");
printTree(root1);
let inverted1 = invertTree(root1);
console.log("Inverted 1 (Expected: [4,7,2,9,6,3,1]):");
printTree(inverted1);

// Test 2: [2,1,3]
let root2 = buildTree([2, 1, 3]);
console.log("Original 2:");
printTree(root2);
let inverted2 = invertTree(root2);
console.log("Inverted 2 (Expected: [2,3,1]):");
printTree(inverted2);
