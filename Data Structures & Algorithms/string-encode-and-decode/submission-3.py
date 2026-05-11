class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        print(res)
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            currLen = ''
            while s[i] != '#':
                currLen += s[i]
                i += 1
            currLen = int(currLen)
            j = 0
            i += 1
            curr = ""
            while j < currLen:
                curr += s[i + j]
                j += 1
            res.append(curr)
            i += j
        
        return res