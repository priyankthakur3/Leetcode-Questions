class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []

        def backtrack_helper(open_n, close_n, string):
            # base condition
            if open_n == close_n == n:
                result.append("".join(string))
            # add open parenthesis
            if open_n < n:
                string.append("(")
                backtrack_helper(open_n + 1, close_n, string)
                string.pop()
            # add close parenthesis if less than open
            if close_n < open_n:
                string.append(")")
                backtrack_helper(open_n, close_n + 1, string)
                string.pop()
            
        backtrack_helper(1, 0 , ["("])
        return result