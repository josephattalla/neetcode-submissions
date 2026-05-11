class Pair:

    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    
    def __init__(self, capacity: int):
        # ARRAY OF SIZE CAPACITY
        self.map = [None] * capacity
        self.size = 0
        self.capacity = capacity

    def hashFunction(self, key):
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:

        # FIND IDX OF KEY 
        idx = self.hashFunction(key)

        # PLACE INTO NEXT AVAILABLE SPOT STARTING AT IDX
        while self.map[idx] and self.map[idx].key != key:
            idx += 1
        
        # INCREMENT SIZE IF ADDING NEW KEY
        if not self.map[idx]:
            self.size += 1

        self.map[idx] = Pair(key, value)

        # RESIZE IF NEEDED
        if self.size == self.capacity // 2:
            self.resize() 

    def get(self, key: int) -> int:
        # FIND IDX OF KEY
        idx = self.hashFunction(key)

        # FIND IN MAP 
        if not self.map[idx]:
            return -1
        while idx < self.capacity:
            if self.map[idx] and self.map[idx].key == key:
                return self.map[idx].value 
            idx += 1

        return -1

    def remove(self, key: int) -> bool:
        # FIND IDX OF KEY
        idx = self.hashFunction(key)

        # FIND & REMOVE KEY
        while idx < self.capacity:
            if self.map[idx] and self.map[idx].key == key:
                self.map[idx] = None
                self.size -= 1
                return True
            idx += 1

        return False
        
    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        print("RESIZE ---- CAPACITY: ", self.capacity)
        # NEW MAP OF CAPACITY * 2
        self.capacity *= 2
        oldMap = self.map
        self.map = [None] * self.capacity
        self.size = 0

        # COPY OVER PREVIOUS MAP WITH NEW HASH
        for element in oldMap:
            if element:
                self.insert(element.key, element.value)
        print("RESIZE ----- NEW CAPACITY: ", self.capacity)