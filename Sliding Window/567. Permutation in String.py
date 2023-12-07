class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        s1_freq , s2_freq = [0] * 26, [0] * 26
        s1_len , s2_len = len(s1) , len(s2)
        
        # initialize intial freq map
        for i in range(len(s1)):
            s1_freq[ord(s1[i]) - ord('a')] += 1
            s2_freq[ord(s2[i]) - ord('a')] += 1
        
        for r in range(s1_len, s2_len):
            
            if s1_freq == s2_freq:
                return True

            # update freq map on movement
            s2_freq[ord(s2[r - s1_len]) - ord('a')] -= 1 # decrease count of current window right element
            s2_freq[ord(s2[r]) - ord('a')] += 1
        
        return s1_freq == s2_freq