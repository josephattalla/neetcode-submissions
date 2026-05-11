class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums or len(nums) == 1:
            return True
        jump = nums[0]
        for i in range(jump):
            if self.canJump(nums[i+1:]):
                return True

        return False