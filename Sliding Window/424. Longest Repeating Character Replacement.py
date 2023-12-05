class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_word = {}
        ans = 0
        left = 0
        for right in range(len(s)):
            count_word[s[right]] = 1 + count_word.get(s[right], 0)
            max_freq = max(count_word.values())
            # check if replaced characters is greater than move window
            while (right - left + 1) - max_freq > k:
                count_word[s[left]] -= 1
                left += 1
                
            ans = max(ans, right - left + 1 )
        return ans