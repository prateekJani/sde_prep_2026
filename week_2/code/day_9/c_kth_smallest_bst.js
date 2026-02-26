// Definition for a binary tree node.
function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val)
    this.left = (left === undefined ? null : left)
    this.right = (right === undefined ? null : right)
}

/**
 * @param {TreeNode} root
 * @param {number} k
 * @return {number}
 */
var kthSmallest = function (root, k) {
    const stack = [];
    let curr = root;
    let n = 0;

    while (curr !== null || stack.length > 0) {
        // Go as far left as possible
        while (curr !== null) {
            stack.push(curr);
            curr = curr.left;
        }

        curr = stack.pop();
        n++;

        if (n === k) {
            return curr.val;
        }

        curr = curr.right;
    }

    return -1;
};

// Example Usage
//      3
//     / \
//    1   4
//     \
//      2
const root1 = new TreeNode(3, new TreeNode(1, null, new TreeNode(2)), new TreeNode(4));
console.log(kthSmallest(root1, 1)); // 1

//       5
//      / \
//     3   6
//    / \
//   2   4
//  /
// 1
const root2 = new TreeNode(5, new TreeNode(3, new TreeNode(2, new TreeNode(1)), new TreeNode(4)), new TreeNode(6));
console.log(kthSmallest(root2, 3)); // 3
