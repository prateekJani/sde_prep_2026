class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
        and removing all non-alphanumeric characters, it reads the same forward and backward.
        Alphanumeric characters include letters and numbers.

        Given a string s, return true if it is a palindrome, or false otherwise.
        """
        # TODO: Implement this using Two Pointers (O(n) time, O(1) space)

        left = 0
        right = len(s) - 1

        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1

        return True

# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(f"Test 1 'A man, a plan, a canal: Panama': {sol.isPalindrome('A man, a plan, a canal: Panama')} (Expected: True)")
    print(f"Test 2 'race a car': {sol.isPalindrome('race a car')} (Expected: False)")
    print(f"Test 3 ' ': {sol.isPalindrome(' ')} (Expected: True)")
