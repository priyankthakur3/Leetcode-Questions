class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.longest = -1
        self.res = set()

        def dfs(idx, res_str, l_count, r_count):

            # base condition
            if idx >= len(s):
                if l_count == r_count:
                    if len(res_str) > self.longest:
                        self.longest = len(res_str)
                        self.res = set()
                        self.res.add("".join(res_str))
                    elif len(res_str) == self.longest:
                        self.res.add("".join(res_str))
            else:
                cur_char = s[idx]
                if cur_char == "(":
                    res_str.append(cur_char)
                    dfs(idx + 1, res_str, l_count + 1, r_count)
                    res_str.pop()
                    dfs(idx + 1, res_str, l_count, r_count)
                elif cur_char == ")":
                    dfs(idx + 1, res_str, l_count, r_count)
                    if l_count > r_count:
                        res_str.append(cur_char)
                        dfs(idx + 1, res_str, l_count, r_count + 1)
                        res_str.pop()
                else:
                    res_str.append(cur_char)
                    dfs(idx + 1, res_str, l_count, r_count)
                    res_str.pop()
        
        dfs(0, [], 0, 0)
        return self.res