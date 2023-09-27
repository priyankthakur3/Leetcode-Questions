# primitive
"""
class MyHashSet:

    def __init__(self):
        self.arr = [None for _ in range(0, 1000001)]

    def add(self, key: int) -> None:
        print(key)
        if(not self.arr[key]):
            self.arr[key] = key

    def remove(self, key: int) -> None:
        if(self.arr[key]):
            t = self.arr[key]
            self.arr[key] = None
            return t
        else:
            return None

    def contains(self, key: int) -> bool:
        return self.arr[key] == key


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
"""


class MyHashSet(object):

    def __hash_key(self, key):
        return key % self.size, key // self.size

    def __init__(self):
        self.size = 1001
        self.bucket = [None for _ in range(self.size)]

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        key1, key2 = self.__hash_key(key)

        if not self.bucket[key1]:
            self.bucket[key1] = [None for _ in range(self.size)]
        self.bucket[key1][key2] = key

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        key1, key2 = self.__hash_key(key)
        if self.bucket[key1]:
            if self.bucket[key1][key2]:
                self.bucket[key1][key2] = None

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        key1, key2 = self.__hash_key(key)
        if self.bucket[key1]:
            return self.bucket[key1][key2] == key
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
