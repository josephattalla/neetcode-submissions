class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n

        for r in reversed(range(m-1)):
            for c in reversed(range(n-1)):
                dp[c] += dp[c+1]
        return dp[0]