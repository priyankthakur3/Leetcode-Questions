class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}

        def helper(i):
            
            # base condition
            if i == len(s):
                return 1
            # base condition
            if s[i] == '0':
                return 0

            if i in dp:
                return dp[i]

            res = helper(i + 1)

            if i + 1 < len(s) and (s[i] == "1" or ( s[i] =="2" and s[i + 1] in "0123456" ) ):
                res += helper(i + 2)
            dp[i] = res
            return res
        return helper(0)