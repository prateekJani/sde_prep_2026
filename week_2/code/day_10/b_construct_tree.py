from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        # Mapping inorder values to their indices for O(1) lookups
        inorder_map = {val: i for i, val in enumerate(inorder)}
        
        # We need an iterator or a mutable counter for the preorder array index
        self.pre_idx = 0
        
        def build(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
                
            # Current root is at preorder[pre_idx]
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            self.pre_idx += 1
            
            # The root splits inorder list
            mid = inorder_map[root_val]
            
            # Subtrees
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            
            return root
            
        return build(0, len(inorder) - 1)

# Example Usage
if __name__ == "__main__":
    sol = Solution()
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    root = sol.buildTree(preorder, inorder)
    print(root.val) # 3
    print(root.left.val) # 9
    print(root.right.val) # 20
