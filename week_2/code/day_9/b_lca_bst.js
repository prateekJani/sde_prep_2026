// Definition for a binary tree node.
function TreeNode(val) {
    this.val = val;
    this.left = this.right = null;
}

/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
var lowestCommonAncestor = function (root, p, q) {
    let curr = root;

    while (curr) {
        if (p.val > curr.val && q.val > curr.val) {
            curr = curr.right;
        } else if (p.val < curr.val && q.val < curr.val) {
            curr = curr.left;
        } else {
            // Divergent path found, or we've hit p or q itself
            return curr;
        }
    }

    return null;
};

// Example Usage
//      6
//    /   \
//   2     8
//  / \   / \
// 0   4 7   9
//    / \
//   3   5
const n0 = new TreeNode(0);
const n2 = new TreeNode(2);
const n3 = new TreeNode(3);
const n4 = new TreeNode(4);
const n5 = new TreeNode(5);
const n6 = new TreeNode(6);
const n7 = new TreeNode(7);
const n8 = new TreeNode(8);
const n9 = new TreeNode(9);

n6.left = n2; n6.right = n8;
n2.left = n0; n2.right = n4;
n4.left = n3; n4.right = n5;
n8.left = n7; n8.right = n9;

console.log(lowestCommonAncestor(n6, n2, n8).val); // 6
console.log(lowestCommonAncestor(n6, n2, n4).val); // 2
