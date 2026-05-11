class MinHeap:
    
    def __init__(self):
        self.heap = []
        self.heap.append(None)


    def percolateUp(self, i):
        # PARENT(I) = I // 2, HEAP[PARENT] < HEAP[I] => SWAP(PARENT, I)
        while i // 2 > 0 and self.heap[i] < self.heap[i // 2]:
            tmp = self.heap[i]
            self.heap[i] = self.heap[i // 2]
            self.heap[i // 2] = tmp
            i = i // 2


    def percolateDown(self, i):
        while 2 * i < len(self.heap): # WHILE CHILDREN EXIST FOR I
            # RCHILD = 2*I + 1, LCHILD = 2*I

            # SWAP RIGHT CHILD IF SMALLEST 
            if 2 * i + 1 < len(self.heap) and self.heap[2 * i + 1] < self.heap[2 * i] and self.heap[i] > self.heap[2 * i + 1]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[2 * i + 1]
                self.heap[2 * i + 1] = tmp
                i = 2 * i + 1
            # SWAP LEFT CHILD IF SMALLEST
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
        
        # REPLACE ROOT W/LAST VALUE AND PERCULATE IT DOWN
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
        
        # PUT FIRST NUMBER IN BACK, SET 0 IDX TO NONE
        self.heap = nums
        self.heap.append(self.heap[0])
        self.heap[0] = None

        # PERCULATE DOWN FROM FIRST NODE W/CHILDREN
        cur = (len(self.heap) - 1) // 2
        while cur > 0:
            self.percolateDown(cur)
            cur -= 1