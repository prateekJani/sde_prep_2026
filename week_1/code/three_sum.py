from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that 
        i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

        Notice that the solution set must not contain duplicate triplets.
        """
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # Skip positive integers (cannot sum to 0 with others since sorted)
            if a > 0:
                break

            # Skip duplicate 'a' values
            if i > 0 and a == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # Skip duplicate 'l' values to avoid same triplet
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res

# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(f"Test 1 [-1,0,1,2,-1,-4]: {sol.threeSum([-1,0,1,2,-1,-4])} (Expected: [[-1,-1,2],[-1,0,1]])")
    print(f"Test 2 [0,1,1]: {sol.threeSum([0,1,1])} (Expected: [])")
    print(f"Test 3 [0,0,0]: {sol.threeSum([0,0,0])} (Expected: [[0,0,0]])")
