# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        
        while curr:
            # If both p and q are greater than the current node's value, LCA is in the right subtree
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # If both p and q are less than the current node's value, LCA is in the left subtree
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            # We found the split point (or one of the nodes is the LCA of the other)
            else:
                return curr

# Example Usage
if __name__ == "__main__":
    sol = Solution()
    
    #      6
    #    /   \
    #   2     8
    #  / \   / \
    # 0   4 7   9
    #    / \
    #   3   5
    
    n0 = TreeNode(0)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n7 = TreeNode(7)
    n8 = TreeNode(8)
    n9 = TreeNode(9)
    
    n6.left, n6.right = n2, n8
    n2.left, n2.right = n0, n4
    n4.left, n4.right = n3, n5
    n8.left, n8.right = n7, n9
    
    # LCA of 2 and 8 is 6
    print(sol.lowestCommonAncestor(n6, n2, n8).val)
    
    # LCA of 2 investments 4 is 2
    print(sol.lowestCommonAncestor(n6, n2, n4).val)
