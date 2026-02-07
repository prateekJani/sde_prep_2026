class Solution:
    def isValid(self, s: str) -> bool:
        """
        Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
        An input string is valid if:
        1. Open brackets must be closed by the same type of brackets.
        2. Open brackets must be closed in the correct order.
        3. Every close bracket has a corresponding open bracket of the same type.
        """
        stack = []
        closeToOpen = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False

# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(f"Test 1 '()': {sol.isValid('()')} (Expected: True)")
    print(f"Test 2 '()[]{{}}': {sol.isValid('()[]{}')} (Expected: True)")
    print(f"Test 3 '(]': {sol.isValid('(]')} (Expected: False)")
    print(f"Test 4 '([])': {sol.isValid('([])')} (Expected: True)")
