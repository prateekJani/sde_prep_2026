import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        # Count task frequencies
        count = Counter(tasks)
        
        # Max-heap to store frequencies (use negative values for heapq)
        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap)
        
        time = 0
        # Queue to store the cooldown: pairs of [remaining_count, unlock_time]
        q = deque()
        
        while max_heap or q:
            time += 1
            
            # If we have tasks to process
            if max_heap:
                # Process the most frequent task
                cnt = 1 + heapq.heappop(max_heap) # +1 because we are dealing with negative numbers
                
                # If there are still instances of this task left
                if cnt != 0:
                    # It will be ready at time + n
                    q.append([cnt, time + n])
            
            # If the task at front of the queue is ready
            if q and q[0][1] == time:
                # Push back into max heap
                heapq.heappush(max_heap, q.popleft()[0])
                
        return time

# Example Usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.leastInterval(["A","A","A","B","B","B"], 2)) # 8
    print(sol.leastInterval(["A","C","A","B","D","B"], 1)) # 6
    print(sol.leastInterval(["A","A","A","B","B","B"], 3)) # 10
