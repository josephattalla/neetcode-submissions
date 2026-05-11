class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        currMax = nums[0]
        currMin = nums[0]

        for num in nums[1:]:
            tmp = currMax * num
            currMax = max(num, tmp, num*currMin)
            currMin = min(num, tmp, num*currMin)
            res = max(res, currMax)
        
        return res 