import random

class RandomizedSet:

    def __init__(self):
        self.numMap = {} # val : index
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.numMap: return False
        self.numMap[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.numMap: return False

        # swap last in the arr w/val to remove
        last_val = self.arr[-1]
        self.arr[-1] = self.arr[self.numMap[val]]
        self.arr[self.numMap[val]] = last_val

        # change index of prev last val in numMap
        self.numMap[last_val] = self.numMap[val]

        # pop value to remove
        self.numMap.pop(val)
        self.arr.pop()

        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()