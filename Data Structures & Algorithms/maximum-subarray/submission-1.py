class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]    
        currSum = 0
        for num in nums:
            # current sum = max(continuing current path, starting new path at num)
            #   starting new path means previous subarray is maxed out
            currSum = max(currSum + num, num)
            maxSum = max(maxSum, currSum)
        return maxSum