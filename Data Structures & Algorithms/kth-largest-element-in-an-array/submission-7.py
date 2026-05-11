class Solution:
    def partition(self, nums, left, right):
        # PARTITION USING RIGHT AS PIVOT
        pivot = nums[right]
        lptr = left

        for i in range(left, right):
            if nums[i] <= pivot:
                nums[i], nums[lptr] = nums[lptr], nums[i]
                lptr += 1
        nums[lptr], nums[right] = pivot, nums[lptr]

        # RETURN PIVOT POSITION
        return lptr

    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k   # IDX OF KTH LARGEST
        left = 0
        right = len(nums) - 1

        while left < right:
            # SORT NUMS
            pivot = self.partition(nums, left, right)


            if k < pivot:   # K IS ON RIGHT PARTITION
                right = pivot - 1
            elif k > pivot: # K IS ON LEFT PARTITION
                left = pivot + 1
            else:
                break
        
        return nums[k]          