# Day 4: Stack

**Goal**: Master Last-In, First-Out (LIFO) operations and recognizing when to "pause" processing to wait for a matching condition (nested structures).

## 1. The Technique
A **Stack** is like a stack of plates. You can only add (`push`) or remove (`pop`) from the top.
-   **Python**: Use a list `[]`. `append()` is push, `pop()` is pop.
-   **JavaScript**: Use an array `[]`. `push()` is push, `pop()` is pop.
-   **Time Complexity**: O(1) for push/pop.

**When to use it:**
-   Parsing nested structures (parentheses, HTML tags).
-   evaluating math expressions.
-   Tracking "history" (undo button, browser back button).
-   "Next Greater Element" problems (Monotonic Stack).

## 2. Problem Set

### A. Valid Parentheses (Easy)
*Check if `()[]{}` are balanced.*
-   **Logic**:
    -   Open bracket? Push to stack.
    -   Close bracket? Check if stack top is the matching open bracket. If so, pop.
    -   End: Stack must be empty.

### B. Min Stack (Medium)
*Design a stack that supports `push`, `pop`, `top`, and retrieving `min` in O(1).*
-   **Technique**: Maintain TWO stacks.
    -   `Main`: Stores actual values.
    -   `Min`: Stores the minimum value seen *so far*.

### C. Evaluate Reverse Polish Notation (Medium)
*Evaluate `["2", "1", "+", "3", "*"]` -> `(2+1)*3` -> `9`.*
-   **Logic**:
    -   Number? Push.
    -   Operator? Pop twice, calculate, push result.

### D. Generate Parentheses (Medium)
*Generate all valid combinations of `n` pairs of parentheses.*
-   **Technique**: Backtracking (Recursion + Stack concept).
    -   Add `(` if `openN < n`.
    -   Add `)` if `closedN < openN`.

---
*Ready to start with Valid Parentheses?*
