class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remaining = {}  # remaining : idx

        for i in range(len(nums)):
            if target - nums[i] in remaining:
                break
            remaining[nums[i]] = i
        
        return [remaining[target - nums[i]], i]