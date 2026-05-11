class Solution:
    # climbStars(n) = climbStairs(n-1) + climbStairs(n-2)
    def climbStairs(self, n: int) -> int:
        if n < 4:
            return n
        
        dp = [2, 3]
        i = 4
        while i <= n:
            dp[0], dp[1] = dp[1], dp[1] + dp[0]
            i += 1
        return dp[1]