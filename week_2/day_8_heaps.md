# Day 8: Heaps / Priority Queues

**Goal**: Understand Heap properties and when to use them (mostly methods involving "Kth" largest/smallest or continuous sorting).

## 1. The Structure
A **Heap** is a complete binary tree.
-   **Min-Heap**: Parent <= Children. Root is minimum.
-   **Max-Heap**: Parent >= Children. Root is maximum.
-   **Operations**:
    -   `push`: O(log n)
    -   `pop`: O(log n) - Removes root.
    -   `peek`: O(1) - Looks at root.
    -   `heapify`: O(n) - Converts array to heap.

**Languages**:
-   **Python**: `heapq` module (Min-Heap by default). For Max-Heap, multiply numbers by -1.
-   **JavaScript**: No built-in Heap! We usually need to implement a simple Heap class or use a library. *For interviews, we might need to write a basic one or assume one exists `MinPriorityQueue`.* We will implement a basic `MinHeap` class for our practice.

## 2. Problem Set

### A. Kth Largest Element in a Stream (Easy)
*Design a class to find the kth largest element in a stream.*
-   **Technique**: Maintain a **Min-Heap** of size `k`. The root is always the Kth largest. If new val > root, pop and push.

### B. Last Stone Weight (Easy)
*Smash heaviest stones together.*
-   **Technique**: **Max-Heap**. Pop two largest (y, x). If x != y, push (y-x).

### C. K Closest Points to Origin (Medium)
*Find K points closest to (0,0).*
-   **Technique**: **Max-Heap** of size K. Store `(-distance, x, y)`. If heap size > K, pop (remove the farthest). Result is the heap. 
    -   *Alternative*: Min-Heap of all points, pop K times (O(N log N) or O(N + K log N)). Max-Heap of size K is O(N log K) -> Better.

### D. Kth Largest Element in an Array (Medium)
*Find Kth largest in generic array.*
-   **Technique**: Min-Heap of size K (O(N log K)). Or QuickSelect (O(N) average). We'll stick to Heap for this day.

### E. Task Scheduler (Medium)
*CPU tasks with cooldown.*
-   **Technique**: **Max-Heap** (frequency) + **Queue** (cooldown). Pop most frequent, process, put in cooldown queue.

### F. Design Twitter (Medium)
*News feed from followees.*
-   **Technique**: user map + **Max-Heap** (most recent tweets). Merge K sorted lists concept.

---
*Ready to build a Heap?*
