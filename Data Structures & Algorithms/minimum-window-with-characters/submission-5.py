class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ret = ""
        subset = {}
        found = {}
        need = len(t)
        have = 0

        for c in t:
            subset[c] = subset.get(c, 0) + 1

        l = 0
        for r in range(len(s)):
            if s[r] in subset:
                found[s[r]] = found.get(s[r], 0) + 1
                if subset[s[r]] >= found[s[r]]:
                    have += 1

            while len(found) == len(subset) and have == need:
                ret = s[l:r+1] if r-l+1 < len(ret) or ret == "" else ret

                if s[l] in found:
                    found[s[l]] -= 1
                    if found[s[l]] < subset[s[l]]:
                        have -= 1
                l += 1
            
        return ret