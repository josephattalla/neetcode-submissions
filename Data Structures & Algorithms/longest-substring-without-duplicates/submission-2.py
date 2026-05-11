class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        seen = set()
        lptr = 0
        rptr = 1
        ret = 1
        seen.add(s[0])

        while rptr < len(s):
            while s[rptr] in seen:
                seen.remove(s[lptr]) 
                lptr += 1
            seen.add(s[rptr]) 
            ret = max(ret, rptr - lptr + 1)
            rptr += 1

        return ret