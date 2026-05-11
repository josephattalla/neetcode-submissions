class Solution:
    def rob(self, nums: List[int]) -> int:
        curr, prev = 0, 0
        for num in nums:
            # best decision = path that robs previous house vs path that robs current house
            temp = max(curr + num, prev)

            # for next iteration 
            curr = prev
            prev = temp
        
        return prev