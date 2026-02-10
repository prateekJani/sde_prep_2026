from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums.
        If target exists, then return its index. Otherwise, return -1.
        
        You must write an algorithm with O(log n) runtime complexity.
        """
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
        return -1

# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(f"Test 1 [-1,0,3,5,9,12], 9: {sol.search([-1,0,3,5,9,12], 9)} (Expected: 4)")
    print(f"Test 2 [-1,0,3,5,9,12], 2: {sol.search([-1,0,3,5,9,12], 2)} (Expected: -1)")
