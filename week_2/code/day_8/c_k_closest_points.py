import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        # Max-heap to store the K closest points. 
        # Since heapq is a min-heap, use negative distance.
        max_heap = []
        
        for x, y in points:
            dist = -(x**2 + y**2)
            if len(max_heap) < k:
                heapq.heappush(max_heap, (dist, x, y))
            elif dist > max_heap[0][0]:
                heapq.heappushpop(max_heap, (dist, x, y))
                
        return [[x, y] for (dist, x, y) in max_heap]

# Example Usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.kClosest([[1, 3], [-2, 2]], 1)) # [[-2, 2]]
    print(sol.kClosest([[3, 3], [5, -1], [-2, 4]], 2)) # [[3, 3], [-2, 4]]
