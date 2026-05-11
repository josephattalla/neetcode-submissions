class MinHeap:
    
    def __init__(self):
        self.heap = []
        self.heap.append(None)


    def percolateUp(self, i):
        while i // 2 > 0 and self.heap[i] < self.heap[i // 2]:
            tmp = self.heap[i]
            self.heap[i] = self.heap[i // 2]
            self.heap[i // 2] = tmp
            i = i // 2


    def percolateDown(self, i):
        while 2 * i < len(self.heap):
            if 2 * i + 1 < len(self.heap) and self.heap[2 * i + 1] < self.heap[2 * i] and self.heap[i] > self.heap[2 * i + 1]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[2 * i + 1]
                self.heap[2 * i + 1] = tmp
                i = 2 * i + 1
            elif self.heap[i] > self.heap[i * 2]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[2 * i]
                self.heap[2 * i] = tmp
                i = 2 * i
            else:
                return


    def push(self, val: int) -> None:
        self.heap.append(val)
        self.percolateUp(len(self.heap) - 1)


    def pop(self) -> int:
        if len(self.heap) == 1:
            return -1
        if len(self.heap) == 2:
            return self.heap.pop()
        
        ret = self.heap[1]
        
        self.heap[1] = self.heap.pop()
        self.percolateDown(1)

        return ret


    def top(self) -> int:
        if len(self.heap) == 1:
            return -1
        return self.heap[1]
        

    def heapify(self, nums: List[int]) -> None:
        if not nums:
            self.heap = []
            self.heap.append(None)
            return
        
        self.heap = nums
        self.heap.append(self.heap[0])
        self.heap[0] = None

        cur = (len(self.heap) - 1) // 2
        while cur > 0:
            self.percolateDown(cur)
            cur -= 1