# One stack solution
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            min_val = val
        else:
            min_val = val if val < self.stack[-1] else self.stack[-1] 
        self.stack.append(val)
        self.stack.append(min_val)


    def pop(self) -> None:
        if len(self.stack) == 0:
            return None
        self.stack.pop()
        self.stack.pop()
        
    def top(self) -> int:
        if len(self.stack) == 0:
            return int('-inf')
        min_val = self.stack.pop()
        top_val = self.stack[-1]
        self.stack.append(min_val)
        return top_val

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return int('-inf')
        return self.stack[-1]        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()