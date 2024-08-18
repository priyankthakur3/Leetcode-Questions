class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.longest = -1
        self.res = set()

        def dfs(idx, res_str, l_count, r_count):

            # base condition
            if idx >= len(s):
                if l_count == r_count:
                    # check if current res_str is greater than previous longest string 
                    if len(res_str) > self.longest:
                        self.longest = len(res_str)
                        # if current string is greater reset res to empty
                        # as we need to eliminate minimum parenthesis
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
                    # append ) only if ( count is greater than r_count
                    if l_count > r_count:
                        res_str.append(cur_char)
                        dfs(idx + 1, res_str, l_count, r_count + 1)
                        res_str.pop()
                # handle if there are any alpha numeric characters in string
                else:
                    res_str.append(cur_char)
                    dfs(idx + 1, res_str, l_count, r_count)
                    res_str.pop()
        
        dfs(0, [], 0, 0)
        return self.res