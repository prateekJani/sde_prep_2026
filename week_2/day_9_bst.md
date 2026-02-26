# Day 9: Binary Search Trees (BST)

**Goal**: Understand the properties of a Binary Search Tree (BST) and how it enables efficient searching, insertion, and validation.

## 1. The Structure
A **Binary Search Tree (BST)** is a binary tree where every node adheres to the following property:
- All nodes in its left subtree have values **strictly less** than the node's value.
- All nodes in its right subtree have values **strictly greater** than the node's value.

This property guarantees that an **in-order traversal (Left, Root, Right)** of a BST yields the nodes' values in a sorted order.

*Time Complexity (Average / Balanced):*
-   **Search**: O(log n)
-   **Insert**: O(log n)
-   **Delete**: O(log n)

*Time Complexity (Worst Case - e.g., straight line tree): O(n)*

## 2. Problem Set

### A. Validate Binary Search Tree (Medium)
*Determine if a valid BST exists.*
-   **Technique**: DFS/Recursion with Bounds. Pass `(min_val, max_val)` down the recursive tree. The root's value must be strictly between these limits. Update limits as you go left (max = root.val) or right (min = root.val). Alternatively, use In-Order Traversal and check if the resulting array is strictly sorted.

### B. Lowest Common Ancestor of a Binary Search Tree (Medium)
*Find the lowest common ancestor (LCA) node of two designated nodes `p` and `q`.*
-   **Technique**: Traverse down from the root. If both `p` and `q` are smaller than root, LCA is in the left subtree. If both are larger, LCA is in the right subtree. Otherwise, the current root is the LCA (the divergence point). This avoids a full DFS.

### C. Kth Smallest Element in a BST (Medium)
*Find the `k`th smallest value in a BST.*
-   **Technique**: **In-Order Traversal**. Since in-order traversal of a BST gives sorted values, simply do an in-order traversal and return the `k`th element visited. Maintain a counter.

---
*Ready to master BSTs?*
