class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:

    def _hash_key(self, value):
        return value % 1000

    def __init__(self):
        self.size = 1001
        self.bucket = [None] * self.size

    def put(self, key: int, value: int) -> None:
        hash_key = self._hash_key(key)
        if self.bucket[hash_key] == None:
            self.bucket[hash_key] = Node(key, value)
        else:
            curr = self.bucket[hash_key]
            while curr:
                if curr.key == key:
                    curr.value = value
                    return
                elif curr.next is None:
                    curr.next = Node(key, value)
                curr = curr.next

    def get(self, key: int) -> int:
        hash_key = self._hash_key(key)
        if self.bucket[hash_key] != None:
            curr = self.bucket[hash_key]
            while curr:
                if curr.key == key:
                    return curr.value
                curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        hash_key = self._hash_key(key)
        if self.bucket[hash_key] is None:
            return None
        prev = None
        curr = self.bucket[hash_key]
        if curr.key == key:
            self.bucket[hash_key] = curr.next
            return
        else:
            while curr:
                if curr.key == key:
                    prev.next = curr.next
                    return
                else:
                    prev = curr
                    curr = curr.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
