from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True
            
        return (self.isSubtree(root.left, subRoot) or 
                self.isSubtree(root.right, subRoot))

    def isSameTree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            return (self.isSameTree(s.left, t.left) and 
                    self.isSameTree(s.right, t.right))
        return False

# Example Usage
if __name__ == "__main__":
    sol = Solution()
    
    # Tree:    3
    #         / \
    #        4   5
    #       / \
    #      1   2
    root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
    
    # subTree:   4
    #           / \
    #          1   2
    subRoot = TreeNode(4, TreeNode(1), TreeNode(2))
    
    print(sol.isSubtree(root, subRoot)) # True
