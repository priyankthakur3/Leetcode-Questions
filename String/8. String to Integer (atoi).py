class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if len(s) == 0:
            return 0
        int_max = 2 ** 31 - 1
        int_min = -2 ** 31
        
        idx = 0
        res = 0
        sign = 1
        if s[0] in ('-', '+'):
            if s[0] == "-":
                sign = -1
            idx += 1
        while idx < len(s):
            t_char = s[idx]
            if not t_char.isdigit():
                break
            t_char = int(t_char)

            # check if res is still within bounds
            if sign == 1 and (res > int_max // 10 or (res == int_max // 10 and t_char > 7 )):
                return int_max
            # check if res is still within bounds
            if sign == -1 and (res > int_max //10 or (res == int_max // 10 and t_char > 8 )):
                return int_min

            res = res * 10 + t_char
            idx += 1
        
        return sign * res