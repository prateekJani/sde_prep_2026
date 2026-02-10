from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
        Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
        Given the sorted rotated array nums of unique elements, return the minimum element of this array.
        You must write an algorithm that runs in O(log n) time.
        """
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            mid = (l + r) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        return res

# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(f"Test 1 [3,4,5,1,2]: {sol.findMin([3,4,5,1,2])} (Expected: 1)")
    print(f"Test 2 [4,5,6,7,0,1,2]: {sol.findMin([4,5,6,7,0,1,2])} (Expected: 0)")
    print(f"Test 3 [11,13,15,17]: {sol.findMin([11,13,15,17])} (Expected: 11)")
