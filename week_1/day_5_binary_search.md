# Day 5: Binary Search

**Goal**: Master O(log n) search algorithms. Learn to discard half of the search space at each step.

## 1. The Technique
Binary Search works on **SORTED** data.
-   **Algorithm**:
    1.  Find the `mid` index: `mid = l + (r - l) // 2`.
    2.  If `target == nums[mid]`, return `mid`.
    3.  If `target > nums[mid]`, search the **Right** half (`l = mid + 1`).
    4.  If `target < nums[mid]`, search the **Left** half (`r = mid - 1`).
-   **Time Complexity**: O(log n).
-   **Checking Condition**: `while l <= r`.

## 2. Problem Set

### A. Binary Search (Easy)
*Basic implementation.*
-   Write the standard algorithm iteratively.

### B. Search a 2D Matrix (Medium)
*Search in a sorted matrix (rows sorted, first int of row > last int of prev row).*
-   **Technique**: Treat the 2D matrix as a flat sorted list or use double binary search (search row, then search col).

### C. Koko Eating Bananas (Medium)
*Find the minimum eating speed `k` to finish all bananas within `h` hours.*
-   **Technique**: Binary Search on the **Answer**.
    -   The possible speeds are `1` to `max(piles)`.
    -   Use BS to find the smallest speed that works.

### D. Find Minimum in Rotated Sorted Array (Medium)
*Array is sorted but rotated (e.g., `[3,4,5,1,2]`). Find min.*
-   **Technique**: Compare `mid` with `right` to see which side is sorted/unsorted.

### E. Search in Rotated Sorted Array (Medium)
*Find target in a rotated sorted array.*
-   **Technique**: Determine which half is sorted first, then check if target lies within that range.

---
*Ready to start with Binary Search?*
