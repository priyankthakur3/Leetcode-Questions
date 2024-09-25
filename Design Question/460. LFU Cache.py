class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = Node

class LRUCache:
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    # add new node at end
    def add(self,node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node
        self.size += 1

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
    
    # remove from head
    def pop(self):
        if self.size == 0:
            return None
        node = self.head.next
        self.remove(node)
        return node
         

class LFUCache:

    def __init__(self, capacity: int):
        self.nodes = {}
        self.freq_map = defaultdict(LRUCache)
        self.capacity = capacity
        self.min_freq = 0
        self.size = 0

    def _update(self, node):
        # get frequency of node
        freq = node.freq
        self.freq_map[freq].remove(node)
        if self.freq_map[freq].size == 0 and self.min_freq == freq:
            self.min_freq += 1
        node.freq += 1
        self.freq_map[node.freq].add(node)

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        node = self.nodes[key]
        self._update(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        if key in self.nodes:
            node = self.nodes[key]
            node.value = value
            self._update(node)
        
        else:
            if self.size == self.capacity:
                lfu_list = self.freq_map[self.min_freq]
                removed_node = lfu_list.pop()
                del self.nodes[removed_node.key]
                self.size -= 1
            
            # new node always gooes at 1 in freq_map
            new_node = Node(key, value)
            self.nodes[key] = new_node
            self.freq_map[1].add(new_node)
            self.min_freq = 1
            self.size+= 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)