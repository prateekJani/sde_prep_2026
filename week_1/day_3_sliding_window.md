# Day 3: Sliding Window

**Goal**: Efficiently handle subsets of data (subarrays/substrings) by maintaining a "window" that slides over the input.
**Key Idea**: converting O(n^2) nested loops into O(n) linear scans.

## 1. The Technique
A **Sliding Window** is a sub-list that runs over an underlying collection.
-   **Fixed Size**: The window size `k` stays constant. (e.g., "Max sum of 3 consecutive elements").
-   **Dynamic Size**: The window grows or shrinks based on constraints. (e.g., "Longest substring with...").

**Pattern:**
1.  Initialize `Left` and `Right` pointers at 0.
2.  Expand `Right` to include new elements.
3.  If the window becomes invalid (constraint broken), increment `Left` (shrink) until it's valid again.
4.  Update the result (usually max length or min length) at each step.

## 2. Problem Set

### A. Best Time to Buy and Sell Stock (Easy)
*Maximize profit by choosing a single day to buy and a different day in the future to sell.*
-   **Technique**: Just track the `min_price` seen so far.
-   It's technically a "One Pass" problem, but can be visualized as a dynamic window where `L=buy_day` and `R=current_day`.

### B. Longest Substring Without Repeating Characters (Medium)
*Find the length of the longest substring without duplicate characters.*
-   **Technique**: Use a Set/Map to track characters in the current window.
-   If `s[R]` is in the set, shrink from `L` (remove `s[L]`) until `s[R]` can be added.
-   Result = `max(Result, R - L + 1)`.

### C. Longest Repeating Character Replacement (Medium)
*You can replace up to k characters. Find longest substring of same letter.*
-   **Technique**: Valid window if `(window_len - count_of_most_frequent_char) <= k`.
-   If invalid, shrink from `L`.

---
*Ready to start with Best Time to Buy and Sell Stock?*
