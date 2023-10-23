class Solution:
    def decodeString(self, s: str) -> str:
        if len(s) == 1:
            return s
        stack = []
        for ch in s:
            # add all elements to stack until we encounter ]
            if ch != "]":
                stack.append(ch)
            # once we encounter ] pop elements
            else:
                substr = ""
                # append all character to substr
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                # remove "[" from stack
                stack.pop()
                # check if there are any digits still pending
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                # append (num * substr) back to stack
                stack.append(int(num) * substr)
            # concat all elements in stack into string
        return "".join(stack)
