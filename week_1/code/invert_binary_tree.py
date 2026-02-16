from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Given the root of a binary tree, invert the tree, and return its root.
        """
        if not root:
            return None
        
        # Swap and recurse
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        
        return root

# Helper to print tree (Level Order) for testing
def printTree(root):
    if not root:
        print("[]")
        return
    queue = [root]
    res = []
    while queue:
        node = queue.pop(0)
        if node:
            res.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        else:
            res.append("null")
    # Clean up trailing nulls
    while res and res[-1] == "null":
        res.pop()
    print("[" + ",".join(res) + "]")

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
    
    # Test 1: [4,2,7,1,3,6,9]
    root1 = buildTree([4,2,7,1,3,6,9])
    print("Original 1:")
    printTree(root1)
    inverted1 = sol.invertTree(root1)
    print("Inverted 1 (Expected: [4,7,2,9,6,3,1]):")
    printTree(inverted1)

    # Test 2: [2,1,3]
    root2 = buildTree([2,1,3])
    print("Original 2:")
    printTree(root2)
    inverted2 = sol.invertTree(root2)
    print("Inverted 2 (Expected: [2,3,1]):")
    printTree(inverted2)
