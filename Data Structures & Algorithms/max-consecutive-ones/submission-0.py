class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        curr = 0

        for i in nums:
            if i: curr += 1
            else:
                res = max(curr, res)
                curr = 0

        res = max(curr, res)
        return res