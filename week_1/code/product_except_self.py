from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Given an integer array nums, return an array answer such that answer[i] is equal to
        the product of all the elements of nums except nums[i].
        
        The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
        
        You must write an algorithm that runs in O(n) time and without using the division operation.
        """
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res

# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(f"Test 1 [1,2,3,4]: {sol.productExceptSelf([1,2,3,4])} (Expected: [24, 12, 8, 6])")
    print(f"Test 2 [-1,1,0,-3,3]: {sol.productExceptSelf([-1,1,0,-3,3])} (Expected: [0, 0, 9, 0, 0])")
