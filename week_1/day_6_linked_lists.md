# Day 6: Linked Lists

**Goal**: Master pointer manipulation. Linked Lists are all about managing references (`next`, `prev`) without losing track of the head.

## 1. The Structure
A **Node** usually looks like this:
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

**Key Patterns:**
1.  **Dummy Node**: Use a `dummy` node at the start of a new list to avoid edge cases (e.g., empty list, inserting at head). Return `dummy.next`.
2.  **Fast & Slow Pointers (Tortoise & Hare)**:
    -   Find middle: Fast moves 2x, Slow moves 1x. When Fast reaches end, Slow is at middle.
    -   Detect Cycle: If Fast meets Slow, there is a cycle.
3.  **Multi-Pointer**: `prev`, `curr`, `next` for reversing.

## 2. Problem Set

### A. Reverse Linked List (Easy)
*Reverse a singly linked list.*
-   **Technique**: Iterative. `curr.next = prev`, then move pointers forward.

### B. Merge Two Sorted Lists (Easy)
*Merge two sorted lists into one sorted list.*
-   **Technique**: Use a `dummy` node and iterate. Compare `list1.val` vs `list2.val`, attach smaller to `current.next`.

### C. Linked List Cycle (Easy)
*Determine if a cycle exists.*
-   **Technique**: Floyd's Cycle Detection (Fast/Slow pointers).

### D. Reorder List (Medium)
*Reorder `L0 -> L1 -> ... -> Ln-1 -> Ln` to `L0 -> Ln -> L1 -> Ln-1 ...`*
-   **Technique**:
    1.  Find Middle.
    2.  Reverse Second Half.
    3.  Merge First Half and Second Half.

### E. Remove Nth Node From End of List (Medium)
*Remove the nth node from the end.*
-   **Technique**: Two pointers. Move `right` pointer `n` steps ahead first. Then move `left` and `right` together until `right` hits the end. `left` is now at the node *before* the removal target.

---
*Ready to start with Reverse Linked List?*
