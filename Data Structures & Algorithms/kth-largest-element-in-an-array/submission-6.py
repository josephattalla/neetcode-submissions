class Solution:
    def partition(self, nums, left, right):
        pivot = nums[right]
        lptr = left

        for i in range(left, right):
            if nums[i] <= pivot:
                nums[i], nums[lptr] = nums[lptr], nums[i]
                lptr += 1
        nums[lptr], nums[right] = pivot, nums[lptr]

        return lptr

    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        left = 0
        right = len(nums) - 1

        while left < right:
            pivot = self.partition(nums, left, right)

            if k < pivot:
                right = pivot - 1
            elif k > pivot:
                left = pivot + 1
            else:
                break
        
        return nums[k]          