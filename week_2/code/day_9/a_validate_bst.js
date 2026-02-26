// Definition for a binary tree node.
function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val)
    this.left = (left === undefined ? null : left)
    this.right = (right === undefined ? null : right)
}

/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isValidBST = function (root) {
    function valid(node, leftBoundary, rightBoundary) {
        if (!node) {
            return true;
        }

        if (node.val <= leftBoundary || node.val >= rightBoundary) {
            return false;
        }

        return (
            valid(node.left, leftBoundary, node.val) &&
            valid(node.right, node.val, rightBoundary)
        );
    }

    return valid(root, -Infinity, Infinity);
};

// Example Usage
// Valid BST
//   2
//  / \
// 1   3
const validRoot = new TreeNode(2, new TreeNode(1), new TreeNode(3));
console.log(isValidBST(validRoot)); // true

// Invalid BST
//   5
//  / \
// 1   4
//    / \
//   3   6
const invalidRoot = new TreeNode(5, new TreeNode(1), new TreeNode(4, new TreeNode(3), new TreeNode(6)));
console.log(isValidBST(invalidRoot)); // false
