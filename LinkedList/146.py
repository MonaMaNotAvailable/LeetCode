# Approach 1: Doubly LinkedList with HashMap for efficient node removal & maintain order
# space O(n) for the hash map storing key-node pairs and O(n) for the doubly linked list storing the nodes
class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # store the keys and their corresponding node
        self.head = Node(0, 0)  # dummy head
        self.tail = Node(0, 0)  # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        """remove a node from the doubly linked list."""
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def _add(self, node: Node):
        """add a node right after the head."""
        next = self.head.next
        node.next = next
        node.prev = self.head
        self.head.next = node
        next.prev = node

    # time O(1): accessing the hash map and updating the doubly linked list (removing and adding a node)
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)  # move the accessed node to the front
            self._add(node)  # add it right after the head
            return node.value  # return the value of the node
        return -1  # if key not found, return -1

    # time O(1): inserting into the hash map, updating the doubly linked list, and removing the least recently used item
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])  # remove the old node if it exists
        node = Node(key, value)  # create a new node
        self._add(node)  # add it to the front
        self.cache[key] = node  # update the cache
        if len(self.cache) > self.capacity:
            # remove the least recently used node
            lru = self.tail.prev
            self._remove(lru)  # remove it from the list
            del self.cache[lru.key]  # remove it from the cache



# # Approach 2: using Python default OrderedDict, less manual pointer manipulation
# space O(n) for storing the key-value pairs
# class LRUCache:
#     def __init__(self, capacity: int):
#         # initialize the cache with a given capacity
#         self.capacity = capacity
#         # use an ordered dictionary to maintain the order of elements
#         self.cache = OrderedDict()

#     # time O(1): accessing and moving the element to the end 
#     def get(self, key: int) -> int:
#         # if the key exists in the cache
#         if key in self.cache:
#             # move the accessed key to the end to mark it as recently used
#             self.cache.move_to_end(key)
#             # return the value associated with the key
#             return self.cache[key]
#         # if the key does not exist, return -1
#         return -1

#     # time O(1): inserting/updating the key-value pair and removing the least recently used item
#     def put(self, key: int, value: int) -> None:
#         # if the key already exists in the cache
#         if key in self.cache:
#             # move the key to the end to mark it as recently used
#             self.cache.move_to_end(key)
#         # add/update the key-value pair in the cache
#         self.cache[key] = value
#         # if the cache exceeds its capacity
#         if len(self.cache) > self.capacity:
#             # remove the first item (least recently used) from the cache
#             self.cache.popitem(last=False)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)