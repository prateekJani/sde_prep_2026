from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Given the roots of two binary trees p and q, write a function to check if they are the same or not.
        Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
        """
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
            
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
    
    # Test 1: p = [1,2,3], q = [1,2,3]
    p1 = buildTree([1,2,3])
    q1 = buildTree([1,2,3])
    print(f"Test 1: {sol.isSameTree(p1, q1)} (Expected: True)")

    # Test 2: p = [1,2], q = [1,null,2]
    p2 = buildTree([1,2])
    q2 = buildTree([1,None,2])
    print(f"Test 2: {sol.isSameTree(p2, q2)} (Expected: False)")
    
    # Test 3: p = [1,2,1], q = [1,1,2]
    p3 = buildTree([1,2,1])
    q3 = buildTree([1,1,2])
    print(f"Test 3: {sol.isSameTree(p3, q3)} (Expected: False)")
