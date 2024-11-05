class Solution:
    def calculate(self, s: str) -> int:
        s.strip()
        operator = '+'
        prev = rSum = i = 0
        while i < len(s):
            currchar = s[i]
            curr = 0
            if currchar.isdigit():
                while i < len(s) and s[i].isdigit():
                    curr = curr * 10 + int(s[i])
                    i += 1
                # move pointer by one position backwards
                i -= 1
                # evaluate operators
                if operator == "+":
                    rSum += curr
                    prev = curr
                elif operator == "-":
                    rSum -= curr
                    prev = - curr
                elif operator == "*":
                    rSum -= prev
                    rSum += prev * curr
                    prev = prev * curr
                elif operator == "/":
                    rSum -= prev
                    rSum += int(prev / curr)
                    prev = int(prev / curr)
            elif currchar != " ":
                operator = currchar
            i += 1
            
        return rSum    