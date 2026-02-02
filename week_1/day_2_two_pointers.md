# Day 2: Two Pointers

**Goal**: Master the art of manipulating indices to save time (usually converting O(n^2) to O(n)).

## 1. The Technique
Instead of a nested loop, we use two pointers to scan the array.
- **Left/Right**: Start at ends, move towards middle. (Great for sorted arrays, palindromes).
- **Fast/Slow**: Detect cycles (Linked Lists), remove duplicates in-place.

## 2. Problem Set

### A. Valid Palindrome (Easy)
*Check if a string is a palindrome, ignoring non-alphanumeric chars.*
- **Naive**: Reverse string `s == s[::-1]`.
- **Two Pointers**: Compare `s[left]` vs `s[right]`. Skip invalid chars. O(1) Space.

### B. 3Sum (Medium)
*Find all unique triplets that verify `nums[i] + nums[j] + nums[k] == 0`.*
- **Logic**: Sort the array! Then iterate `i` and use Two Pointers (Left/Right) for the remaining two numbers (like Two Sum II).
- **Tricky Part**: Avoiding duplicates in the result.

### C. Container With Most Water (Medium)
*Find two lines that together with the x-axis form a container, such that the container contains the most water.*
- **Logic**: Maximizing Area. Start max width (L=0, R=end).
- **Move Rule**: Always move the pointer with the *smaller* height (trying to find a taller line to compensate for width loss).

---
*Ready to start with Concepts or Valid Palindrome?*
