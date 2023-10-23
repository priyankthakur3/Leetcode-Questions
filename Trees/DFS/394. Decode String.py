class Solution:
    def decodeString(self, s: str) -> str:
        if len(s) == 1:
            return s

        stack = []
        # initialize currentString and number to empty string and 0
        currStr, currNo = "", "0"

        for ch in s:
            # character is digit add to currNo
            if ch.isdigit():
                currNo = currNo + ch

            # append curStr and currNo to stack and reset currStr and currNo
            elif ch == "[":
                stack.append(currStr)
                stack.append(currNo)
                currStr, currNo = "", "0"

            # pop currStr and currNo and multiply currStr with popped number
            elif ch == "]":
                number = stack.pop()
                tempStr = stack.pop()
                currStr = tempStr + int(number) * currStr

            # else add character to currentStr
            else:
                currStr += ch

        return currStr
