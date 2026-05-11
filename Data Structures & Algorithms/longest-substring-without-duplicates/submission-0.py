class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        length = 0
        lptr = 0
        for rptr in range(len(s)):
            while s[rptr] in seen:
                seen.remove(s[lptr])
                lptr += 1
            
            seen.add(s[rptr])
            length = max(length, rptr - lptr + 1)
        
        return length