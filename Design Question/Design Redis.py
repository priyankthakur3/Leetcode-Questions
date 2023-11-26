class TimeMap:

    def __init__(self):
        self.hash_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.hash_map:
            self.hash_map[key] = []
        self.hash_map[key].append([timestamp,value])
        

    def get(self, key: str, timestamp: int) -> str:

        val = self.hash_map.get(key,[])
        res = ""
        l , r = 0, len(val) - 1

        while l <= r:
            m = l + (r - l) // 2
            # if timestamp is equal or less tan timestamp update res and move l
            if val[m][0] == timestamp:
                return val[m][1]
                # keep moving left until its closer to timestamp
            elif val[m][0] < timestamp:
                res = val[m][1]
                l = m + 1
            else:
                r = m - 1
        return res
        

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)