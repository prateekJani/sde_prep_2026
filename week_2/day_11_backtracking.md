# Day 11: Backtracking

**Goal**: Understand the Backtracking paradigm, which involves exhaustive search (often visualized as decision trees) but with "pruning" to avoid exploring invalid paths.

## 1. The Strategy
Backtracking is essentially a DFS on a conceptual "decision tree" of all possible options.
1.  **Choose**: Pick an option (e.g., add a number to the current combination).
2.  **Explore**: Recursively call the backtrack function with this new state.
3.  **Un-choose**: Revert the choice (e.g., remove the number from the combination) to explore other parallel options.

Key elements of a backtracking function:
-   **Base Case**: When should we stop and add our current path to the result set? (e.g., when the combination size equals `k`, or when we reach the end of the string).
-   **Loop/Choices**: What are the valid next steps from the current state?
-   **Pruning**: Can we stop exploring this branch early? (e.g., if our current sum exceeds the target sum).

*Time Complexity*: Often O(2^N) or O(N!) depending on the number of choices and branches, which is why backtracking problems usually have small input sizes (like N <= 20).

## 2. Problem Set

### A. Subsets (Medium)
*Given an integer array `nums` of unique elements, return all possible subsets (the power set).*
-   **Technique**: For each element, we have a binary choice: include it in the current subset, or don't include it.

### B. Combination Sum (Medium)
*Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations where the chosen numbers sum to `target`. You may choose the same number an unlimited number of times.*
-   **Technique**: Similar to subsets, but we can reuse the current element. Our "choice" is whether to pick the current element again (without advancing the index) or skip the current element (advance the index). Prune if `current_sum > target`.

### C. Permutations (Medium)
*Given an array `nums` of distinct integers, return all the possible permutations.*
-   **Technique**: At each step, we can pick any number we haven't picked yet. We can maintain a `used` boolean array or dynamically pass the remaining choices. Time complexity is O(N * N!).

### D. Word Search (Medium)
*Given an `m x n` grid of characters `board` and a string `word`, return `true` if `word` exists in the grid (horizontally or vertically adjacent cells).*
-   **Technique**: Typical 2D grid DFS backtracking. Maintain a `visited` set (or temporarily mark the board cell as `#`) to avoid re-using the same cell in a single word path. Un-mark it after exploring.

---
*Ready to backtrack?*
