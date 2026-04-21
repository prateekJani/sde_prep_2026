class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        subset = []
        
        def dfs(i):
            if i >= len(nums):
                # Make a copy since subset is modified
                res.append(subset.copy())
                return
            
            # Decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            
            # Decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1)
            
        dfs(0)
        return res

# Example Usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.subsets([1, 2, 3]))
    # [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]
    
    print(sol.subsets([0]))
    # [[0], []]
