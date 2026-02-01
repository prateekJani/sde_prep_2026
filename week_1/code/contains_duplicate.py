from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Given an integer array nums, return true if any value appears at least twice in the array,
        and return false if every element is distinct.
        """
        # TODO: Implement this

        duplicate = {}

        for num in nums:
            if num in duplicate:
                return True
            duplicate[num] = True
        return False



# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(f"Test 1 [1,2,3,1]: {sol.containsDuplicate([1,2,3,1])} (Expected: True)")
    print(f"Test 2 [1,2,3,4]: {sol.containsDuplicate([1,2,3,4])} (Expected: False)")
    print(f"Test 3 [1,1,1,3,3,4,3,2,4,2]: {sol.containsDuplicate([1,1,1,3,3,4,3,2,4,2])} (Expected: True)")
