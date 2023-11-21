class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for token in tokens:
            if token not in ['+','-',"/","*"]:
                stack.append(token)
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if token == "+":
                    stack.append(num1 + num2)
                elif token == "-":
                    stack.append(num1 - num2)
                elif token == "*":
                    stack.append(num1 * num2)
                elif token == "/":
                    stack.append(num1 / num2)
        
        return int(stack.pop())
        