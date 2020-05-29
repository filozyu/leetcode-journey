from collections import OrderedDict


class LRUCache:
    """
    Least recently used cache
    Store up to capacity number of key-value pairs (keys are unique)
    Used meaning an operation (either get or put) has taken place
    Remove the least recently used pair (when there is no key clashes) if put will result in cache above capacity
    Update an existing pair (when key already exists in cache) if put will result in cache above capacity
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        """
        Time: O(1)
        """
        if self.cache.get(key):
            # move_to_end suggest key is recently used
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        """
        Time: O(1)
        """
        if self.cache.get(key):
            # when there is a key clash
            self.cache.move_to_end(key)
            self.cache[key] = value
        elif len(self.cache) < self.capacity:
            # no key clash, under capacity
            self.cache[key] = value
        else:
            # no key clash, above capacity
            # remove the first pair (least recently used)
            self.cache.popitem(last=False)
            self.cache[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
