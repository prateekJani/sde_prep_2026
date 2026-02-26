from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left_boundary, right_boundary):
            if not node:
                return True
            
            # The current node's value must be strictly between the boundaries
            if not (left_boundary < node.val < right_boundary):
                return False
            
            # Left child must be strictly less than node.val
            # Right child must be strictly greater than node.val
            return (valid(node.left, left_boundary, node.val) and
                    valid(node.right, node.val, right_boundary))

        return valid(root, float("-inf"), float("inf"))

# Example Usage
if __name__ == "__main__":
    sol = Solution()
    
    # Valid BST
    #   2
    #  / \
    # 1   3
    valid_root = TreeNode(2, TreeNode(1), TreeNode(3))
    print(sol.isValidBST(valid_root)) # True
    
    # Invalid BST
    #   5
    #  / \
    # 1   4
    #    / \
    #   3   6
    invalid_root = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    print(sol.isValidBST(invalid_root)) # False
