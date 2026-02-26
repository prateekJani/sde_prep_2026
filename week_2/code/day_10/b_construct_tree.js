// Definition for a binary tree node.
function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val)
    this.left = (left === undefined ? null : left)
    this.right = (right === undefined ? null : right)
}

/**
 * @param {number[]} preorder
 * @param {number[]} inorder
 * @return {TreeNode}
 */
var buildTree = function (preorder, inorder) {
    // Map of inorder elements to indices for O(1) lookup
    const inorderMap = new Map();
    for (let i = 0; i < inorder.length; i++) {
        inorderMap.set(inorder[i], i);
    }

    let preIndex = 0;

    function build(left, right) {
        if (left > right) return null;

        const rootVal = preorder[preIndex++];
        const root = new TreeNode(rootVal);

        // Find index of root in inorder array
        const mid = inorderMap.get(rootVal);

        root.left = build(left, mid - 1);
        root.right = build(mid + 1, right);

        return root;
    }

    return build(0, inorder.length - 1);
};

// Example Usage
const preorder = [3, 9, 20, 15, 7];
const inorder = [9, 3, 15, 20, 7];
const root = buildTree(preorder, inorder);
console.log(root.val); // 3
console.log(root.left.val); // 9
console.log(root.right.val); // 20
