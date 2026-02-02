from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        You are given an integer array height of length n. 
        There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
        Find two lines that together with the x-axis form a container, such that the container contains the most water.
        Return the maximum amount of water a container can store.
        """
        # TODO: Implement using Two Pointers (O(n))

        left = 0
        right = len(height)-1
        max_area = 0

        while(left<right):
            width = right - left
            area = width * min(height[left], height[right])
            max_area = max(area, max_area)
            

            if (height[left]<height[right]):
                left+=1
            else:
                right-=1

        return max_area

# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(f"Test 1 [1,8,6,2,5,4,8,3,7]: {sol.maxArea([1,8,6,2,5,4,8,3,7])} (Expected: 49)")
    print(f"Test 2 [1,1]: {sol.maxArea([1,1])} (Expected: 1)")
