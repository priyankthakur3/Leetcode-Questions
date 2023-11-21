class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis_dict = {
            "]" : "[",
            ")" : "(",
            "}" : "{"
        }
        stack = []
        for ch in s:
            if ch in parenthesis_dict:
                if len(stack) > 0 and stack[-1] == parenthesis_dict[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        return len(stack) == 0
