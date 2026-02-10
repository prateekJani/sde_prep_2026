from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Koko loves to eat bananas. There are n piles of bananas given by the array piles.
        Koko can decide her bananas-per-hour eating speed of k.
        Each hour, she chooses some pile of bananas and eats k bananas from that pile.
        If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
        
        Return the minimum integer k such that she can eat all the bananas within h hours.
        """
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            
            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        
        return res

# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(f"Test 1 [3,6,7,11], h=8: {sol.minEatingSpeed([3,6,7,11], 8)} (Expected: 4)")
    print(f"Test 2 [30,11,23,4,20], h=5: {sol.minEatingSpeed([30,11,23,4,20], 5)} (Expected: 30)")
    print(f"Test 3 [30,11,23,4,20], h=6: {sol.minEatingSpeed([30,11,23,4,20], 6)} (Expected: 23)")
