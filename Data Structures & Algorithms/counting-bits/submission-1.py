class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)    
        offset = 1  # offset from previous same number number with 1 less 1 bit
        # base case: 0, alr filled
        for num in range(1, n+1):
            if num == offset << 1:  # if current number is a new power of 2, set as offset
                offset = num
            dp[num] = dp[num - offset] + 1
        return dp