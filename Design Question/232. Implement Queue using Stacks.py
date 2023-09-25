# Time Complexity
# push: O(1)
# pop: O(n) worst case, otherwise O(1)
# peek: O(n) worst case, otherwise O(1)
class MyQueue:

    # all input will fall in input
    # all peek and pop will occur from output stack
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        # accept into input
        self.input.append(x)

    def pop(self) -> int:
        self.peek()
        return self.output.pop()

    def peek(self) -> int:
        # check if output stack is empty if yes move all content from input to output
        if len(self.output) == 0:
            while len(self.input) != 0:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self) -> bool:
        return self.input == [] and self.output == []


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
