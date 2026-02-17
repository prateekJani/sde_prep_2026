from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Given the root of a binary tree, return its maximum depth.
        A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
        """
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# Helper to build tree from level order list
def buildTree(arr):
    if not arr: return None
    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    while queue and i < len(arr):
        node = queue.pop(0)
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
    return root

# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: [3,9,20,null,null,15,7]
    root1 = buildTree([3,9,20,None,None,15,7])
    print(f"Test 1 Max Depth: {sol.maxDepth(root1)} (Expected: 3)")

    # Test 2: [1,null,2]
    root2 = buildTree([1,None,2])
    print(f"Test 2 Max Depth: {sol.maxDepth(root2)} (Expected: 2)")
