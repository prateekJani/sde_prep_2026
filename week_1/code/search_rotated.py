from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        There is an integer array nums sorted in ascending order (with distinct values).
        Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length).
        Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
        You must write an algorithm with O(log n) runtime complexity.
        """
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            # Check if left half is sorted
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # Right half is sorted
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(f"Test 1 [4,5,6,7,0,1,2], 0: {sol.search([4,5,6,7,0,1,2], 0)} (Expected: 4)")
    print(f"Test 2 [4,5,6,7,0,1,2], 3: {sol.search([4,5,6,7,0,1,2], 3)} (Expected: -1)")
    print(f"Test 3 [1], 0: {sol.search([1], 0)} (Expected: -1)")
