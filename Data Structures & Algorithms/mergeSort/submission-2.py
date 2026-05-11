# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

def merge(pairs, s, m, e):
    left = pairs[s:m+1]
    right = pairs[m+1:e+1]

    i = 0
    j = 0
    k = s

    while i < len(left) and j < len(right):
        if left[i].key <= right[j].key:
            pairs[k] = left[i]
            i += 1
        else:
            pairs[k] = right[j]
            j += 1
        k += 1
    
    while i < len(left):
        pairs[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        pairs[k] = right[j]
        j += 1
        k += 1


class Solution:
    def mergeHelper(self, pairs, s, e):
        # base case: end index <= start index
        if e <= s:
            return
        
        # get middle index
        m = (e + s) // 2

        # sort left side
        self.mergeHelper(pairs, s, m)

        # sort right side
        self.mergeHelper(pairs, m+1, e)

        # merge both sorted sides
        merge(pairs, s, m, e)

    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        self.mergeHelper(pairs, 0, len(pairs))
        return pairs