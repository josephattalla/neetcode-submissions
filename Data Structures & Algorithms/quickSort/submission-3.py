# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSortHelper(self, pairs, s, e):
        # base case: single number, e <= s
        if e <= s:
            return

        # 1. choose pivot
        pivot = e

        # 2. put pairs[i] < pivot on left side
        start = s
        for i in range(s, e):
            if pairs[i].key < pairs[pivot].key:
                pairs[start], pairs[i] = pairs[i], pairs[start]
                start += 1

        # 3. put pivot b/w left & right side
        pairs[start], pairs[pivot] = pairs[pivot], pairs[start]

        # 4. quicksort left & right side
        self.quickSortHelper(pairs, s, start-1)
        self.quickSortHelper(pairs, start+1, e)

    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs)-1)
        return pairs