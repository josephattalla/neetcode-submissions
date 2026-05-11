class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 1. make dp grid w/extra col & row to account for filling in edges 
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        # 2.  bottom up approach --- starting in bottom right corner 
        #     matching char => dp[r][c] = dp[r+1][c+1] + 1 to account for double counting same letter
        #     not matching => dp[r][c] = max(dp[r+1][c], dp[r][c+1]) to account for new matches in row and col
        for r in reversed(range(len(text1))):
            for c in reversed(range(len(text2))):
                if text1[r] == text2[c]:
                    dp[r][c] = dp[r+1][c+1] + 1
                else:
                    dp[r][c] = max(dp[r+1][c], dp[r][c+1])

        return dp[0][0]

