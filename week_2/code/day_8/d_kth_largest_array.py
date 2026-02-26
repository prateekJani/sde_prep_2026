import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # Min-heap of size K
        min_heap = nums[:k]
        heapq.heapify(min_heap)
        
        for num in nums[k:]:
            if num > min_heap[0]:
                heapq.heappushpop(min_heap, num)
                
        return min_heap[0]

# Example Usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.findKthLargest([3,2,1,5,6,4], 2)) # 5
    print(sol.findKthLargest([3,2,3,1,2,4,5,5,6], 4)) # 4
