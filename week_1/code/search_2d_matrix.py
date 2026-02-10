from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        You are given an m x n integer matrix matrix with the following two properties:
        1. Each row is sorted in non-decreasing order.
        2. The first integer of each row is greater than the last integer of the previous row.
        
        Given an integer target, return true if target is in matrix or false otherwise.
        You must write a solution in O(log(m * n)) time complexity.
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, ROWS * COLS - 1

        while l <= r:
            mid = (l + r) // 2
            mid_val = matrix[mid // COLS][mid % COLS]

            if mid_val > target:
                r = mid - 1
            elif mid_val < target:
                l = mid + 1
            else:
                return True
        return False

# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(f"Test 1 Found: {sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)} (Expected: True)")
    print(f"Test 2 Not Found: {sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13)} (Expected: False)")
