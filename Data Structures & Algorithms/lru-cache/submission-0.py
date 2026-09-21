class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        # map from key to node
        # can access node at whatever position in ordered list
        # can remove node and append to front in constant time
        self.cache = defaultdict(Node)
        self.capacity = capacity

        # real head of list = self.head.next
        self.head = Node("head", "head")
        # real tail of the list = self.tail.prev
        self.tail = Node("tail", "tail")
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.removeNode(node)
        self.addToHead(node)
        return node.val
    
    def removeNode(self, node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def addToHead(self, node) -> None:
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        node.next.prev = node

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.removeNode(node)
            node.val = value
            self.addToHead(node)
            return
        
        node = Node(key, value)
        self.cache[key] = node
        self.addToHead(node)

        if len(self.cache) > self.capacity:
            node = self.tail.prev
            self.removeNode(node)
            del self.cache[node.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)