from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Given n non-negative integers representing an elevation map where the width of each bar is 1,
        compute how much water it can trap after raining.
        """
        if not height: return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res


# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(f"Test 1 [0,1,0,2,1,0,1,3,2,1,2,1]: {sol.trap([0,1,0,2,1,0,1,3,2,1,2,1])} (Expected: 6)")
    print(f"Test 2 [4,2,0,3,2,5]: {sol.trap([4,2,0,3,2,5])} (Expected: 9)")
