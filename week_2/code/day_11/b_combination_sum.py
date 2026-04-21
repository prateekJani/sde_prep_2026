class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        
        def dfs(i, current_comb, total):
            # Base Cases
            if total == target:
                res.append(current_comb.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            # Decision 1: Include candidates[i] (and stay at index i to reuse it)
            current_comb.append(candidates[i])
            dfs(i, current_comb, total + candidates[i])
            
            # Decision 2: Do NOT include candidates[i] (and move to next index i + 1)
            current_comb.pop()
            dfs(i + 1, current_comb, total)
            
        dfs(0, [], 0)
        return res

# Example Usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.combinationSum([2, 3, 6, 7], 7)) # [[2, 2, 3], [7]]
    print(sol.combinationSum([2, 3, 5], 8))    # [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    print(sol.combinationSum([2], 1))          # []
