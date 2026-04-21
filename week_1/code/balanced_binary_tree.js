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
 * @return {boolean}
 */
var isBalanced = function (root) {
    function dfs(node) {
        if (!node) return 0;

        let left = dfs(node.left);
        if (left === -1) return -1;

        let right = dfs(node.right);
        if (right === -1) return -1;

        if (Math.abs(left - right) > 1) return -1;

        return 1 + Math.max(left, right);
    }

    return dfs(root) !== -1;
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
// Test 1: [3,9,20,null,null,15,7] (Balanced)
let root1 = buildTree([3, 9, 20, null, null, 15, 7]);
console.log("Test 1:", isBalanced(root1), "(Expected: true)");

// Test 2: [1,2,2,3,3,null,null,4,4] (Unbalanced)
let root2 = buildTree([1, 2, 2, 3, 3, null, null, 4, 4]);
console.log("Test 2:", isBalanced(root2), "(Expected: false)");
