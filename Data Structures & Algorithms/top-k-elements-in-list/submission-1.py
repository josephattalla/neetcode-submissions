class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums))]

        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for num, i in count.items():
            print(num, i)
            freq[i - 1].append(num)
        
        res = []
        for bucket in reversed(freq):
            for num in bucket:
                res.append(num)
                if len(res) == k:
                    return res
        
        return []