# Day 1: Arrays & Hashing

**Goal**: Understand not just how to use arrays/maps, but *why* they work the way they do (memory layout, collision handling) and how to analyze their efficiency.

## 1. Concepts Checklist
- [ ] **RAM Model**: Understand how arrays are stored contiguously in memory.
- [ ] **Big O Notation**:
    - **Time Complexity**: O(1) vs O(n) vs O(n^2) vs O(log n).
    - **Space Complexity**: Stack memory vs Heap memory.
- [ ] **Hash Maps/Sets**:
    - How they achieve O(1) average lookup.
    - Handling Collisions: Chaining vs Open Addressing.
    - Worst case scenarios (O(n)).

## 2. Problem Set (Warm-up to Application)

### A. Contains Duplicate (Easy)
*Check if any integer appears at least twice in the array.*
- **Naive**: Nested loops -> O(n^2).
- **Sorting**: Sort first, check adjacent -> O(n log n).
- **HashSet**: Iterate and store -> O(n) Time, O(n) Space.

### B. Valid Anagram (Easy)
*Given two strings s and t, return true if t is an anagram of s.*
- **Technique**: Frequency Map (Hash Map) or fixed size array (int[26]) since characters are limited.

### C. Two Sum (Easy)
*Find two numbers that add up to a target.*
- **Naive**: Checking all pairs.
- **Optimized**: Use a Map to store {value : index} as you iterate. Check if `target - current_value` exists in the map.

### D. Product of Array Except Self (Medium)
*Return an array where output[i] is the product of all elements except nums[i]. No division allowed.*
- **Constraint**: O(n) time.
- **Technique**: Prefix Product Array and Suffix Product Array (or calculate on the fly).
