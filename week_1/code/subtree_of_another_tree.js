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
 * @param {TreeNode} subRoot
 * @return {boolean}
 */
var isSubtree = function (root, subRoot) {
    if (!subRoot) return true;
    if (!root) return false;

    if (isSameTree(root, subRoot)) return true;

    return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
};

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
// Test 1: root = [3,4,5,1,2], subRoot = [4,1,2] (True)
let root1 = buildTree([3, 4, 5, 1, 2]);
let subRoot1 = buildTree([4, 1, 2]);
console.log("Test 1:", isSubtree(root1, subRoot1), "(Expected: true)");

// Test 2: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2] (False)
let root2 = buildTree([3, 4, 5, 1, 2, null, null, null, null, 0]);
let subRoot2 = buildTree([4, 1, 2]);
console.log("Test 2:", isSubtree(root2, subRoot2), "(Expected: false)");
