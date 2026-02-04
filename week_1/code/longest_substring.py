class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Given a string s, find the length of the longest substring without repeating characters.
        """
        # TODO: Implement using Sliding Window + Set
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        
        return res

# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(f"Test 1 'abcabcbb': {sol.lengthOfLongestSubstring('abcabcbb')} (Expected: 3)")
    print(f"Test 2 'bbbbb': {sol.lengthOfLongestSubstring('bbbbb')} (Expected: 1)")
    print(f"Test 3 'pwwkew': {sol.lengthOfLongestSubstring('pwwkew')} (Expected: 3)")
