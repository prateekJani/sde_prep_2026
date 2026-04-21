# Day 7: Trees

**Goal**: Master recursion and tree traversal (DFS/BFS).

## 1. The Structure
A **Node** usually looks like this:
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

## 2. Key Concepts
1.  **Recursion**: The heart of tree problems. Solve the problem for the left child, then the right child, then combine.
    -   *Base Case*: Usually `if not root: return ...`
2.  **DFS (Depth-First Search)**: Go deep. Pre-order, In-order, Post-order.
3.  **BFS (Breadth-First Search)**: Go wide (Level Order). Uses a Queue.

## 3. Problem Set

### A. Invert Binary Tree (Easy)
*Swap left and right children for every node.*
-   **Technique**: Recursion. `root.left, root.right = invert(root.right), invert(root.left)`.

### B. Maximum Depth of Binary Tree (Easy)
*Find the longest path from root to leaf.*
-   **Technique**: `1 + max(dfs(root.left), dfs(root.right))`.

### C. Diameter of Binary Tree (Easy)
*Longest path between any two nodes (may not pass through root).*
-   **Technique**: DFS. At each node, calculate height. Diameter at that node is `left_height + right_height`. Update a global `max_diameter`.

### D. Balanced Binary Tree (Easy)
*Height of left and right subtrees differ by no more than 1.*
-   **Technique**: DFS returning height. If `abs(left - right) > 1`, return -1 (or flag as unbalanced).

### E. Same Tree (Easy)
*Check if two trees are structurally identical and have the same values.*
-   **Technique**: Recursion. `if p.val == q.val and isSame(p.left, q.left) and isSame(p.right, q.right)`.

### F. Subtree of Another Tree (Easy)
*Check if `subRoot` is a subtree of `root`.*
-   **Technique**: Traverse `root`. For each node, check if it's `isSameTree` with `subRoot`.

---
*Ready to start with Invert Binary Tree?*
