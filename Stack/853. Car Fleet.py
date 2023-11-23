class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [ [p,s] for p,s in zip(position,speed)]
        stack = []
        ans = 0
        for p, s in sorted(cars,reverse=True):
            curr = (target - p) / s
            # if stack empty or time taken is greater than last car
            if len(stack) == 0 or curr > stack[-1]:
                stack.append(curr)
        return len(stack)