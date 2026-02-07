from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
        """
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == n and closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res

# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(f"Test 1 n=3: {sol.generateParenthesis(3)} (Expected: ['((()))','(()())','(())()','()(())','()()()'])")
    print(f"Test 2 n=1: {sol.generateParenthesis(1)} (Expected: ['()'])")
