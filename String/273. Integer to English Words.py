class Solution:
    def numberToWords(self, num: int) -> str:
        
        # edge case
        if num == 0:
            return "Zero"

        # mapping for nums below 20
        ones_mapping = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen"
        }

        # tens mapping
        tens_mapping = {
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety"
        }


        def getString(n):
            s = []
            hundreds = n // 100
            if hundreds:
                s.append(ones_mapping[hundreds] + ' Hundred')
            last_2 = n % 100
            # check tens and ones exists
            if last_2 >= 20:
                tens = last_2 // 10
                ones = last_2 % 10
                s.append(tens_mapping[tens * 10])
                if ones:
                    s.append(ones_mapping[ones])
            elif last_2:
                s.append(ones_mapping[last_2])
            return " ".join(s)
        
        thousands_mapping = ["", " Thousand", " Million", " Billion"]
        i = 0
        res = []
        while num:
            digits = num % 1000
            d_s = getString(digits) 
            # edge case 
            # 1000000
            if d_s:
                res.append(d_s + thousands_mapping[i])
            i += 1
            num = num // 1000
        res.reverse()
        return " ".join(res)
