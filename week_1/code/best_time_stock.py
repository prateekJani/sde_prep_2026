from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        You are given an array prices where prices[i] is the price of a given stock on the ith day.
        You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
        Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
        """
        # TODO: Implement using Sliding Window (or just tracking min_price)

        l, r = 0, 1

        profit = 0

        while(r<len(prices)):
            if prices[l] < prices[r]:
                profit = max(prices[r] - prices[l], profit)
            else:
                l = r
            r += 1

        
        return profit

        pass

# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(f"Test 1 [7,1,5,3,6,4]: {sol.maxProfit([7,1,5,3,6,4])} (Expected: 5)")
    print(f"Test 2 [7,6,4,3,1]: {sol.maxProfit([7,6,4,3,1])} (Expected: 0)")
