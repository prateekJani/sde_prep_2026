from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
        """
        if not subRoot: return True
        if not root: return False
        
        if self.isSameTree(root, subRoot):
            return True
            
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        if not p or not q or p.val != q.val: return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

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
    
    # Test 1: root = [3,4,5,1,2], subRoot = [4,1,2] (True)
    root1 = buildTree([3,4,5,1,2])
    subRoot1 = buildTree([4,1,2])
    print(f"Test 1: {sol.isSubtree(root1, subRoot1)} (Expected: True)")

    # Test 2: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2] (False)
    root2 = buildTree([3,4,5,1,2,None,None,None,None,0])
    subRoot2 = buildTree([4,1,2])
    print(f"Test 2: {sol.isSubtree(root2, subRoot2)} (Expected: False)")
