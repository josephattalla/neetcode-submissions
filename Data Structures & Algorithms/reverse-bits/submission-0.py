class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in reversed(range(32)):
            bit = n & 1
            n = n >> 1
            res |= bit << i
        return res