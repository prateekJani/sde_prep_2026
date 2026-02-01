class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Given two strings s and t, return true if t is an anagram of s, and false otherwise.
        
        An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
        typically using all the original letters exactly once.
        """
        # TODO: Implement this

        if len(s) != len(t):
            return False

        hash_s = {}
        hash_t = {}

        for char in s:
            hash_s[char] = hash_s.get(char, 0) + 1
        
        for char in t:
            hash_t[char] = hash_t.get(char, 0) + 1

        return hash_s == hash_t

# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(f"Test 1 (anagram, nagaram): {sol.isAnagram('anagram', 'nagaram')} (Expected: True)")
    print(f"Test 2 (rat, car): {sol.isAnagram('rat', 'car')} (Expected: False)")
