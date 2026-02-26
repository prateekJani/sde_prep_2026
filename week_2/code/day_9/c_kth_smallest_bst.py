from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        n = 0
        
        while curr or stack:
            # Go as far left as possible
            while curr:
                stack.append(curr)
                curr = curr.left
                
            # Pop and process
            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val
                
            # Go right
            curr = curr.right
            
        return -1

# Example Usage
if __name__ == "__main__":
    sol = Solution()
    
    #      3
    #     / \
    #    1   4
    #     \
    #      2
    root1 = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
    print(sol.kthSmallest(root1, 1)) # 1
    
    #       5
    #      / \
    #     3   6
    #    / \
    #   2   4
    #  /
    # 1
    root2 = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))
    print(sol.kthSmallest(root2, 3)) # 3
