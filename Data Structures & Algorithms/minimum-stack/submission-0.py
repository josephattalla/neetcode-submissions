class MinStack:

    def __init__(self):
        self.mainStack = []
        self.currMinStack = []

    def push(self, val: int) -> None:
        self.mainStack.append(val)
        
        if not self.currMinStack or val < self.currMinStack[-1]:
            self.currMinStack.append(val)
        else:
            self.currMinStack.append(self.currMinStack[-1])

    def pop(self) -> None:
        self.currMinStack.pop()
        self.mainStack.pop()

    def top(self) -> int:
        return self.mainStack[-1]

    def getMin(self) -> int:
        return self.currMinStack[-1]
