import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        # Python's heapq is a min-heap, so we use negative values for a max-heap
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        
        while len(max_heap) > 1:
            stone1 = heapq.heappop(max_heap) # heaviest (most negative)
            stone2 = heapq.heappop(max_heap) # second heaviest
            
            if stone1 != stone2:
                # stone1 is more negative, so stone1 < stone2. 
                # The remaining weight is stone1 - stone2 (which is negative)
                # It correctly represents the new stone weight in terms of our max-heap
                heapq.heappush(max_heap, stone1 - stone2)
                
        return -max_heap[0] if max_heap else 0

# Example Usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.lastStoneWeight([2, 7, 4, 1, 8, 1])) # Should output 1
