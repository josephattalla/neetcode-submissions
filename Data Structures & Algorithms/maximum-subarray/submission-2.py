class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest = nums[0]
        curr = 0

        for num in nums:
            curr = max(curr + num, num)
            largest = max(curr, largest)
        
        return largest