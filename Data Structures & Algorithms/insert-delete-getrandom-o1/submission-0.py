import random

class RandomizedSet:

    def __init__(self):
        self.storage = {} # val : index
        self.indices = {} # index : val
        self.size = 0

    def insert(self, val: int) -> bool:
        if val in self.storage: return False
        self.storage[val] = self.size
        self.indices[self.size] = val
        self.size += 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.storage: return False
        i = self.storage[val]
        self.storage.pop(val)
        self.indices.pop(i)
        return True

    def getRandom(self) -> int:
        i = random.randint(0, self.size)
        while i not in self.indices:
            i = random.randint(0, self.size)
        return self.indices[i]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()