class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_log = []
        digit_log = []

        for log in logs:
            data = log.split(" ")
            # if second part contains number then add to digit log
            if data[1].isnumeric():
                digit_log.append(log)
            else:
                letter_log.append(log)
        # sort based on content then key
        # maxsplit maximum split strings to get
        letter_log.sort(key=lambda w: (w.split(maxsplit=1)[1],w.split(maxsplit=1)[0] )) 
        return letter_log + digit_log