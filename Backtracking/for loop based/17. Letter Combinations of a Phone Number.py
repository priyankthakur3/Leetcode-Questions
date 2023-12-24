class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []
        res = []

        number_combination = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        def helper(idx, combination):
            
            if idx == len(digits):
                res.append("".join(combination))
                return
            
            letters = number_combination[digits[idx]]

            for letter in letters:
                combination.append(letter)
                helper(idx + 1, combination)
                combination.pop()
        
        helper(0, [])
        return res
