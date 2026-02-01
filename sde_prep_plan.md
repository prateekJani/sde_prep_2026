# 8-Week SDE Preparation Plan: DSA & System Design

This plan is designed to take you from a baseline understanding to interview-ready for top-tier tech companies (FAANG, Unicorns, etc.). It requires **3-4 hours/day** of reliable effort.

## Phase 1: Data Structures & Algorithms Core (Weeks 1-4)
**Goal**: Master the patterns, not just individual problems.

### Week 1: Foundational Data Structures
*   **Day 1: Arrays & Hashing**
    *   *Concept*: RAM model, complexity analysis, hash map internals.
    *   *Problems*: Two Sum, Contains Duplicate, Product of Array Except Self, Valid Anagram.
*   **Day 2: Two Pointers & Sliding Window**
    *   *Concept*: Reducing nested loops to O(n).
    *   *Problems*: 3Sum, Container With Most Water, Best Time to Buy and Sell Stock, Longest Substring Without Repeating Characters.
*   **Day 3: Stack & Queue**
    *   *Concept*: LIFO/FIFO, Monotonic Stack.
    *   *Problems*: Valid Parentheses, Daily Temperatures, Min Stack, Evaluate Reverse Polish Notation.
*   **Day 4: Binary Search**
    *   *Concept*: Search space reduction.
    *   *Problems*: Binary Search, Search a 2D Matrix, Koko Eating Bananas, Find Minimum in Rotated Sorted Array.
*   **Day 5: Linked Lists**
    *   *Concept*: Pointer manipulation, cycle detection (Floyd’s).
    *   *Problems*: Reverse Linked List, Merge Two Sorted Lists, Reorder List, Linked List Cycle, Remove Nth Node From End of List.
*   **Day 6: Review & Contest**
    *   Re-do any problems you struggled with.
    *   Participate in a timed virtual contest (LeetCode Weekly format).
*   **Day 7: Rest / Light Reading** (Read about Time Complexity Big-O thoroughly).

### Week 2: Trees & Recursion
*   **Day 8: Trees Basics (DFS/BFS)**
    *   *Concept*: Traversal orders (Pre/In/Post), Level Order.
    *   *Problems*: Invert Binary Tree, Maximum Depth of Binary Tree, Diameter of Binary Tree, Level Order Traversal.
*   **Day 9: Binary Search Trees (BST)**
    *   *Concept*: BST properties, validation.
    *   *Problems*: Validate BST, Lowest Common Ancestor of a BST, Kth Smallest Element in a BST.
*   **Day 10: Advanced Trees & Tries**
    *   *Concept*: Prefix trees.
    *   *Problems*: Subtree of Another Tree, Construct Binary Tree from Preorder and Inorder Traversal, Implement Trie (Prefix Tree).
*   **Day 11: Backtracking**
    *   *Concept*: Decision trees, pruning.
    *   *Problems*: Subsets, Combination Sum, Permutations, Word Search.
*   **Day 12: Heaps / Priority Queues**
    *   *Concept*: Min/Max heap properties, Heapify.
    *   *Problems*: Kth Largest Element in an Array, Task Scheduler, Design Twitter, Find Median from Data Stream.
*   **Day 13: Review & Contest**
*   **Day 14: Rest**

### Week 3: Graphs & Advanced Structures
*   **Day 15: Graphs Basics**
    *   *Concept*: Adjacency List/Matrix, DFS/BFS on Graphs.
    *   *Problems*: Number of Islands, Max Area of Island, Clone Graph.
*   **Day 16: Advanced Graphs (Topology & Cycles)**
    *   *Concept*: Topological Sort (Kahn’s), Union-Find.
    *   *Problems*: Course Schedule I & II, Pacific Atlantic Water Flow, Number of Connected Components in an Undirected Graph.
*   **Day 17: Shortest Paths**
    *   *Concept*: Dijkstra’s Algorithm, Bellman-Ford (basics).
    *   *Problems*: Network Delay Time, Cheapest Flights Within K Stops.
*   **Day 18: Intervals & Geometry**
    *   *Problems*: Insert Interval, Merge Intervals, Non-overlapping Intervals, Rotate Image.
*   **Day 19: Bit Manipulation**
    *   *Concept*: XOR tricks, bit shifting.
    *   *Problems*: Single Number, Number of 1 Bits, Counting Bits, Missing Number, Sum of Two Integers.
*   **Day 20: Review & Contest**
*   **Day 21: Rest**

### Week 4: Dynamic Programming & Greedy
*   **Day 22: 1-D Dynamic Programming**
    *   *Concept*: Memoization vs Tabulation.
    *   *Problems*: Climbing Stairs, House Robber I & II, Longest Palindromic Substring, Decode Ways.
*   **Day 23: 2-D Dynamic Programming**
    *   *Concept*: Grid DP, Knapsack problem.
    *   *Problems*: Unique Paths, Longest Common Subsequence, Best Time to Buy and Sell Stock with Cooldown, Coin Change.
*   **Day 24: Greedy Algorithms**
    *   *Concept*: Local optimum vs Global optimum.
    *   *Problems*: Maximum Subarray, Jump Game I & II, Gas Station, Partition Labels.
*   **Day 25: Buffer Day / Hard Problems**
    *   Try "Hard" versions of Week 1-3 topics (e.g., Trapping Rain Water, Sliding Window Maximum).
*   **Day 26-27: Comprehensive Revision**
    *   Revisit the "Blind 75" list checklist. Ensure you can solve 90% of them without hints.
*   **Day 28: Rest**

---

## Phase 2: System Design & Polish (Weeks 5-8)
**Goal**: Learn to build scalable systems and articulate trade-offs.

### Week 5: System Design Concepts (HLD)
*   **Day 29: Networking & APIs**
    *   *Topics*: HTTP/HTTPS, TCP/UDP, REST vs GraphQL vs gRPC, WebSockets.
*   **Day 30: Scalability Basics**
    *   *Topics*: Vertical vs Horizontal Scaling, Load Balancers (L4 vs L7), Consistent Hashing.
*   **Day 31: Databases**
    *   *Topics*: SQL (ACID) vs NoSQL (BASE), CAP Theorem, Sharding, Replication (Master-Slave, Multi-Master).
*   **Day 32: Caching & Asynchronism**
    *   *Topics*: Caching Strategies (Write-through, Write-back), Eviction policies (LRU), Message Queues (Kafka/RabbitMQ).
*   **Day 33: Major Case Studies - I**
    *   *Design*: URL Shortener (TinyURL), Pastebin.
    *   *Focus*: ID generation, database selection.
*   **Day 34: Major Case Studies - II**
    *   *Design*: Chat System (WhatsApp/Telegram).
    *   *Focus*: Real-time communication, status updates, storage.
*   **Day 35: Rest**

### Week 6: Low-Level Design (LLD) & OOPS
*   **Day 36: OOPS Principles**
    *   *Topics*: Encapsulation, Polymorphism, Inheritance, Abstraction.
*   **Day 37: SOLID Principles**
    *   *Topics*: Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion.
*   **Day 38: Design Patterns - I (Creational)**
    *   *Patterns*: Singleton, Factory, Builder.
*   **Day 39: Design Patterns - II (Structural/Behavioral)**
    *   *Patterns*: Adapter, Observer, Strategy, Decorator.
*   **Day 40: LLD Problems - I**
    *   *Problem*: Design a Parking Lot.
*   **Day 41: LLD Problems - II**
    *   *Problem*: Design an Elevator System / Tic-Tac-Toe.
*   **Day 42: Rest**

### Week 7: Advanced System Design & Integration
*   **Day 43: Major Case Studies - III**
    *   *Design*: Video Streaming (YouTube/Netflix).
    *   *Focus*: CDN, Chunking, Adaptive bitrate streaming.
*   **Day 44: Major Case Studies - IV**
    *   *Design*: Ride Sharing (Uber/Lyft).
    *   *Focus*: Geo-hashing (QuadTrees), matching algorithms.
*   **Day 45: Major Case Studies - V**
    *   *Design*: E-commerce (Amazon).
    *   *Focus*: Inventory management, heavy read/write concurrency.
*   **Day 46: Distributed System Concepts**
    *   *Topics*: Distributed Transactions (2PC, Sagas), Leader Election, MapReduce basics.
*   **Day 47-48: Mixed Practice**
    *   Pick a random system and design it on a whiteboard/paper in 45 mins.
    *   Self-critique: Did you discuss trade-offs?
*   **Day 49: Rest**

### Week 8: Mock Interviews & Final Polish
*   **Day 50-54: Mock Interviews**
    *   Schedule 1 mock interview per day (use Pramp, Interviewing.io, or friends).
    *   Alternate between Coding and System Design.
*   **Day 55: Behavioral Prep**
    *   Prepare stories for "Tell me about a time..." using the **STAR** method (Situation, Task, Action, Result).
*   **Day 56: Final Rest & Mental Prep**

## Recommended Resources
*   **Coding**: LeetCode (Blind 75 & NeetCode 150 lists).
*   **System Design**: "System Design Interview" by Alex Xu (Vol 1 & 2), "Designing Data-Intensive Applications" (Martin Kleppmann - for depth).
*   **LLD**: "Head First Design Patterns" or Refactoring.Guru.
