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
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
var isSameTree = function (p, q) {
    if (!p && !q) return true;
    if (!p || !q || p.val !== q.val) return false;

    return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
};

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
// Test 1: p = [1,2,3], q = [1,2,3]
let p1 = buildTree([1, 2, 3]);
let q1 = buildTree([1, 2, 3]);
console.log("Test 1:", isSameTree(p1, q1), "(Expected: true)");

// Test 2: p = [1,2], q = [1,null,2]
let p2 = buildTree([1, 2]);
let q2 = buildTree([1, null, 2]);
console.log("Test 2:", isSameTree(p2, q2), "(Expected: false)");

// Test 3: p = [1,2,1], q = [1,1,2]
let p3 = buildTree([1, 2, 1]);
let q3 = buildTree([1, 1, 2]);
console.log("Test 3:", isSameTree(p3, q3), "(Expected: false)");
