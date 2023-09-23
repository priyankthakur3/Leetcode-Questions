class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


# new/recently used node at end
# least node used at start

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        # dummy nodes
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add(self, node):

        # add new node at end of double linkedlist
        prev_node = self.tail.prev
        prev_node.next = node
        self.tail.prev = node
        node.prev = prev_node
        node.next = self.tail

    def _remove(self, node):
        # update pointers
        node.prev.next = node.next
        node.next.prev = node.prev
        node = None

    def get(self, key: int) -> int:
        # if key is present
        if key in self.map:
            node = self.map[key]
            # bring node to end to indicate currently accessed
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:

        # if key exists in list remove existing
        if key in self.map:
            self._remove(self.map[key])

        # create new node and add to dictonary
        node = Node(key, value)
        self._add(node)
        self.map[key] = node

        # check if len is greater if yes remove node at begin
        if len(self.map) > self.capacity:
            head_node = self.head.next
            self._remove(head_node)
            del self.map[head_node.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
