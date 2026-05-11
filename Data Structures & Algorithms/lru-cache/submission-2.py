class Node:

    def __init__(self, key, value, next=None, previous=None):
        self.key = key
        self.value = value
        self.next = next
        self.previous = previous


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # DICTIONARY POINTING TO NODE
        self.cache = {}
        # HEAD.next = MRU, TAIL.prev = LRU
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.previous = self.head
        
    def insert(self, node):

        # PLACE NODE AS MRU
        if not self.cache:
            self.head.next = node
            node.previous = self.head
            self.tail.previous = node
            node.next = self.tail
        else:
            prevHead = self.head.next
            prevHead.previous = node
            node.next = prevHead
            self.head.next = node
            node.previous = self.head

        self.cache[node.key] = node
    
    def delete(self, node):
        if node.key not in self.cache:
            return

        node = self.cache[node.key]
        nodePrev = node.previous
        nodeNext = node.next
        nodePrev.next = nodeNext
        nodeNext.previous = nodePrev

        del self.cache[node.key]

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1 
        
        node = self.cache[key]
        self.delete(node)
        self.insert(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.delete(self.cache[key])
        
        self.insert(Node(key, value))

        if len(self.cache) > self.capacity:
            self.delete(self.tail.previous)