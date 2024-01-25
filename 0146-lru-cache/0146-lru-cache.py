class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = self.prev = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.left, self.right = Node(0,0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
        self.cap = capacity
        self.map = {}

    def remove(self, node):
        prev, nxt = node.prev, node.next
        node.prev.next, node.next.prev = nxt, prev
        
    def insert(self, node):
        prev, right = self.right.prev, self.right
        prev.next = node
        right.prev = node
        node.prev = prev
        node.next = right
        
    def get(self, key: int) -> int:
        if key in self.map:
            self.remove(self.map[key])
            self.insert(self.map[key])
            return self.map[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.remove(self.map[key])
        self.map[key] = Node(key, value)
        self.insert(self.map[key])
        
        if len(self.map) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.map[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)