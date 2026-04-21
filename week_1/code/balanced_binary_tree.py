from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Given a binary tree, determine if it is height-balanced.
        For this problem, a height-balanced binary tree is defined as:
        a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
        """
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            if left == -1: return -1
            
            right = dfs(node.right)
            if right == -1: return -1
            
            if abs(left - right) > 1:
                return -1
                
            return 1 + max(left, right)
            
        return dfs(root) != -1

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
    
    # Test 1: [3,9,20,null,null,15,7] (Balanced)
    root1 = buildTree([3,9,20,None,None,15,7])
    print(f"Test 1: {sol.isBalanced(root1)} (Expected: True)")

    # Test 2: [1,2,2,3,3,null,null,4,4] (Unbalanced)
    root2 = buildTree([1,2,2,3,3,None,None,4,4])
    print(f"Test 2: {sol.isBalanced(root2)} (Expected: False)")
