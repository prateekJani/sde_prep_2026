from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        You can return the answer in any order.
        """
        # TODO: Implement this
        prev_map = {} 

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prev_map:
                return [prev_map[diff], i]
            prev_map[n] = i
        return []


# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(f"Test 1 [2,7,11,15], 9: {sol.twoSum([2,7,11,15], 9)} (Expected: [0, 1])")
    print(f"Test 2 [3,2,4], 6: {sol.twoSum([3,2,4], 6)} (Expected: [1, 2])")
    print(f"Test 3 [3,3], 6: {sol.twoSum([3,3], 6)} (Expected: [0, 1])")
