class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in reversed(range(32)):
            bit = n & 1 # get lsb from n
            n = n >> 1  # get rid of lsb in n
            res |= bit << i # put lsb from on opposite side in result
        return res