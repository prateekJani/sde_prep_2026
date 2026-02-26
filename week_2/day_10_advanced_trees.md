# Day 10: Advanced Trees & Tries

**Goal**: Move beyond standard Binary Search Trees to handle slightly more complex tree constructions and learn a new structure: the Trie (Prefix Tree).

## 1. Advanced Trees
In previous days, we dealt mainly with traversals and properties. Now we'll look at constructing trees from traversals and comparing subtrees.

-   **Preorder (Root, Left, Right) + Inorder (Left, Root, Right)**: These two traversals together are sufficient to uniquely reconstruct a binary tree. The first element of Preorder is always the root. The position of that element in the Inorder array tells you how many nodes are in the left vs right subtrees.
-   **Subtrees**: Checking if tree T is a subtree of tree S usually involves finding a node in S that matches the root of T, and then doing a simultaneous pre-order traversal starting from both nodes to verify they are exactly identical.

## 2. Tries (Prefix Trees)
A **Trie** is a specialized tree used mainly for efficiently storing and retrieving keys in a dataset of strings.
-   Each node represents a character.
-   Useful for features like **autocomplete**, spell checking, and long-prefix matching.
-   Instead of storing the entire string in a node, the path down the tree represents the string.
-   Nodes often have an `is_end_of_word` boolean flag.

*Time Complexity*: O(M) where M is the length of the string for insert, search, and startsWith operations.

## 3. Problem Set

### A. Subtree of Another Tree (Easy)
*Given the roots of two binary trees `root` and `subRoot`, check if `subRoot` is a subtree of `root`.*
-   **Technique**: Write a helper function `isSameTree(p, q)`. Then recursively check if `root` is identical to `subRoot`, OR if `subRoot` is a subtree of `root.left`, OR if `subRoot` is a subtree of `root.right`.

### B. Construct Binary Tree from Preorder and Inorder Traversal (Medium)
*Build the tree using two arrays.*
-   **Technique**: The first item in `preorder` is the root. Find this root in `inorder`. Everything to the left in `inorder` belongs to the left subtree, and everything to the right belongs to the right subtree. Recursively build `left` and `right`.
-   **Optimization**: Use a HashMap to store the value-to-index mapping for the `inorder` array to give O(1) lookups instead of O(N) linear scans.

### C. Implement Trie (Prefix Tree) (Medium)
*Design a Trie class with `insert`, `search`, and `startsWith` methods.*
-   **Technique**: Create a `TrieNode` class containing a hash map (or fixed array of size 26) of children nodes and an `is_word` boolean. Start from the root and traverse down for each character in the word.

---
*Ready to build some Tries?*
