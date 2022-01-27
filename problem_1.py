class Node:
    def __init__(self, value):
        self.prev = None
        self.next = None
        self.value = value

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

MAX_CACHE_CAPACITY = 1000
class LRU_Cache(object):
    def __init__(self, capacity):
        # Initialize class variables
        if capacity <= 0:
            raise ValueError('Error: Cache capacity must be > 0')

        if capacity > MAX_CACHE_CAPACITY:
            raise ValueError(f'Error: Cache capacity must be <= {MAX_CACHE_CAPACITY} to prevent excessive cache memory usage')

        self.capacity = capacity
        self.cache = dict()
        self.dll = DoublyLinkedList()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.cache:
            self.__update_cache_activity(key)
            return self.cache[key].value
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key in self.cache: # overwrite if already in the cache
            self.cache[key].value = value
        else:
            if len(self.cache) == self.capacity:
                self.__remove_oldest_item()
            self.cache[key] = Node(value)

        self.__update_cache_activity(key)

    def __update_cache_activity(self, key):
        cur_node = self.cache[key]
        if not cur_node:
            return

        if cur_node == self.dll.head: # node is already the most recent
            return

        prev_node = cur_node.prev
        next_node = cur_node.next
        cur_head = self.dll.head

        # update doubly linked list head and tail
        if not self.dll.tail:
            self.dll.tail = cur_node
        elif cur_node == self.dll.tail: # there has to be a cur_node.next otherwise this would also be the head and the function would have returned
            self.dll.tail = cur_node.next

        self.dll.head = cur_node

        # update pointers for nodes
        if prev_node:
            prev_node.next = cur_node.next

        if next_node:
            next_node.prev = cur_node.prev

        cur_node.prev = cur_head
        cur_node.next = None

        if cur_head:
            cur_head.next = cur_node

    def __remove_oldest_item(self):
        oldest_item = self.dll.tail

        if oldest_item:
            del self.cache[oldest_item.value]

            self.dll.tail = oldest_item.next
            if oldest_item == self.dll.head:
                self.dll.head = None # since the oldest item is being deleted

            # cleanup links
            oldest_item.next = None
            # oldest item has no previous (it's first)
            if self.dll.tail:
                self.dll.tail.prev = None

# Test Cases

##########
# Test Case 1: Nominal set, get, and least recently used replacement behavior
tc1_cache = LRU_Cache(5)

tc1_cache.set(1, 1);
tc1_cache.set(2, 2);
tc1_cache.set(3, 3);
tc1_cache.set(4, 4);

tc1_cache.get(1)
tc1_cache.get(2)
tc1_cache.get(9)

tc1_cache.set(5, 5)
tc1_cache.set(6, 6)

print('Test Case 1')
print(tc1_cache.get(3))
# Expected Output: -1 because the cache reached capacity and 3 was the least recently used entry
print(tc1_cache.get(6))
# Expected Output: 6 because this replaced 3 when the cache reached its capacity
print('----------')

##########
# Test Case 2: Set a value that is already in the cache
tc2_cache = LRU_Cache(3)

tc2_cache.set(1, 1);
tc2_cache.set(2, 2);
tc2_cache.set(2, 2);
tc2_cache.set(2, 2);
tc2_cache.set(2, 2);
tc2_cache.set(2, 2);
tc2_cache.set(3, 3);

print('Test Case 2')
print(tc2_cache.get(1))
# Expected Output: 1; the multiple sets for 2 should not have resulted in 1 being removed
print(tc2_cache.get(2))
# Expected Output: 2
print(tc2_cache.get(3))
# Expected Output: 3
tc2_cache.set(4, 4);
print(tc2_cache.get(1))
# Expected Output: -1 because the cache reached capacity and 1 was the least recently used entry
print(tc2_cache.get(4))
# Expected Output: 4 because this replaced 1 when the cache reached its capacity
print('----------')

##########
# Test Case 3: Cache of 1
tc3_cache = LRU_Cache(1)

tc3_cache.set(1, 1);

print('Test Case 3')
print(tc3_cache.get(1))
# Expected Output: 1; cache is now full
tc3_cache.set(2, 2);
print(tc3_cache.get(1))
# Expected Output: -1 because the cache reached capacity and 1 was the least recently used entry
print(tc3_cache.get(2))
# Expected Output: 2 because this replaced 1 when the cache reached its capacity
print('----------')

##########
# Test Case 4: Emptry String And None For Keys And Values
tc4_cache = LRU_Cache(4)
tc4_cache.set('', 1); # Empty string key
tc4_cache.set(2, ''); # Empty string value
tc4_cache.set(None, 3); # None key
tc4_cache.set(4, None); # None value

print('Test Case 4')
print(tc4_cache.get(''))
# Expected Output: 1
print(tc4_cache.get(2))
# Expected Output: '' (empty string)
print(tc4_cache.get(None))
# Expected Output: 3
print(tc4_cache.get(4))
# Expected Output: None
print('----------')

##########
# Test Case 5: Overwrite Existing Value In The Cache
tc5_cache = LRU_Cache(3)
tc5_cache.set(1, 1);
tc5_cache.set(2, 2);
tc5_cache.set(3, 3);
tc5_cache.set(1, 10);

print('Test Case 5')
print(tc5_cache.get(1))
# Expected Output: 10 since the original value of 1 was overwritten
print(tc5_cache.get(2))
# Expected Output: 2 since should not have been affected when 1 was overwritten
print(tc5_cache.get(3))
# Expected Output: 3 since should not have been affected when 1 was overwritten
tc5_cache.set(1, 100);
tc5_cache.set(4, 4);
print(tc5_cache.get(1))
# Expected Output: 100 since the value of 10 was overwritten
print(tc5_cache.get(2))
# Expected Output: -1 because the cache reached capacity and 2 was the least recently used entry
print(tc5_cache.get(3))
# Expected Output: 3 since should have been unaffected by the overwrite of 10 and removal of the least recently used entry (2)
print(tc5_cache.get(4))
# Expected Output: 4 because this replaced 10 when the cache reached its capacity
print('----------')

##########
# Test Case 6: Cache Capacity Is 0
print('Test Case 6')
try:
    tc6_cache = LRU_Cache(0)
except ValueError as tc6_err:
    print(tc6_err)
# Expected Output: Error: Cache capacity must be > 0
print('----------')

##########
# Test Case 7: Cache Capacity Is Negative
print('Test Case 7')
try:
    tc7_cache = LRU_Cache(-42)
except ValueError as tc7_err:
    print(tc7_err)
# Expected Output: Error: Cache capacity must be > 0
print('----------')

##########
# Test Case 8: Cache Capacity Is Too Large
print('Test Case 8')
try:
    tc8_cache = LRU_Cache(1e6)
except ValueError as tc8_err:
    print(tc8_err)
# Expected Output: Error: Cache capacity must be <= 1000 to prevent excessive cache memory usage
