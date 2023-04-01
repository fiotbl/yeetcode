class Node:
    def __init__(self, key: int, value: int):
        self.key, self.value = key, value
        self.next = self.prev = None
        
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    # remove from left side
    def remove(self, node):
        nxt, prev = node.next, node.prev
        nxt.prev, prev.next = prev, nxt
    
    def insert(self, node):
        nxt, prev = self.right, self.right.prev
        nxt.prev = prev.next = node
        node.prev, node.next = prev,nxt
    
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)
            
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)