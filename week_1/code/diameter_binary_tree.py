from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Given the root of a binary tree, return the length of the diameter of the tree.
        The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
        This path may or may not pass through the root.
        The length of a path between two nodes is represented by the number of edges between them.
        """
        # TODO: Implement DFS to find diameter
        pass

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
    
    # Test 1: [1,2,3,4,5]
    root1 = buildTree([1,2,3,4,5])
    print(f"Test 1: {sol.diameterOfBinaryTree(root1)} (Expected: 3)")

    # Test 2: [1,2]
    root2 = buildTree([1,2])
    print(f"Test 2: {sol.diameterOfBinaryTree(root2)} (Expected: 1)")
