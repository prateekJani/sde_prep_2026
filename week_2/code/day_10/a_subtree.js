// Definition for a binary tree node.
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

    if (isSameTree(root, subRoot)) {
        return true;
    }

    return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
};

const isSameTree = function (s, t) {
    if (!s && !t) return true;
    if (s && t && s.val === t.val) {
        return isSameTree(s.left, t.left) && isSameTree(s.right, t.right);
    }
    return false;
};

// Example Usage
// Tree:    3
//         / \
//        4   5
//       / \
//      1   2
const root = new TreeNode(3, new TreeNode(4, new TreeNode(1), new TreeNode(2)), new TreeNode(5));

// subTree:   4
//           / \
//          1   2
const subRoot = new TreeNode(4, new TreeNode(1), new TreeNode(2));

console.log(isSubtree(root, subRoot)); // true
