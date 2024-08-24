class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        # build all available numbers
        self.numbers = set(range(maxNumbers))

    def get(self) -> int:
        # get number
        if len(self.numbers) > 0:
            return self.numbers.pop()
        return -1
        
    def check(self, number: int) -> bool:
        # check if number is available
        return number in self.numbers

    def release(self, number: int) -> None:
        # recycle number
        self.numbers.add(number)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)