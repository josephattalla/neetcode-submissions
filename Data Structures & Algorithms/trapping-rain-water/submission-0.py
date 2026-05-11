class Solution:
    def trap(self, height: List[int]) -> int:
        lptr = 0
        rptr = len(height) - 1
        lmax = height[0]
        rmax = height[rptr]
        total = 0

        while lptr < rptr:
            if lmax < rmax:
                lptr += 1
                water = lmax - height[lptr]
                total += water if water > 0 else 0
                lmax = max(lmax, height[lptr])
            else:
                rptr -= 1
                water = rmax - height[rptr]
                total += water if water > 0 else 0
                rmax = max(rmax, height[rptr])
        
        return total
