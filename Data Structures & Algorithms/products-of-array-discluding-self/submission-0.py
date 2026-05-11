class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lprod = [1] * len(nums)
        rprod = [1] * len(nums)

        for i in range(1, len(nums)):
            lprod[i] = lprod[i-1] * nums[i-1]
        for i in range(len(nums) - 2, -1, -1):
            rprod[i] = rprod[i+1] * nums[i+1]
        
        ret = []
        for i in range(len(nums)):
            ret.append(lprod[i] * rprod[i])
        
        return ret
        