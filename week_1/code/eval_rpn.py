from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Evaluate the value of an arithmetic expression in Reverse Polish Notation.
        Valid operators are +, -, *, and /. Each operand may be an integer or another expression.
        Note that division between two integers should truncate toward zero.
        """
        stack = []
        for t in tokens:
            if t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            elif t == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(t))
        return stack[0]

# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(f"Test 1 ['2','1','+','3','*']: {sol.evalRPN(['2','1','+','3','*'])} (Expected: 9)")
    print(f"Test 2 ['4','13','5','/','+']: {sol.evalRPN(['4','13','5','/','+'])} (Expected: 6)")
    print(f"Test 3 ['10','6','9','3','+','-11','*','/','*','17','+','5','+']: {sol.evalRPN(['10','6','9','3','+','-11','*','/','*','17','+','5','+'])} (Expected: 22)")
