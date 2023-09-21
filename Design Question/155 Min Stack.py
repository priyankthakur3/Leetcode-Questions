class MinStack:

    def __init__(self):
        self.original = []
        self.minStack = []    

    def push(self, val: int) -> None:
        self.original.append(val)
        if(len(self.minStack) ==0 or val < self.minStack[-1]):
            self.minStack.append(val)
        else:
            self.minStack.append(self.minStack[-1])

    def pop(self) -> None:
        self.original.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.original[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]