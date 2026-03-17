from test_runner import assert_equal, run_tests

'''
146. LRU Cache

Implement the Least Recently Used (LRU) cache class LRUCache.

Operations:
- LRUCache(capacity): Initialize cache of size capacity.
- get(key): Return value for key if exists, else -1.
- put(key, value): Update or add. If over capacity, evict least recently used.
- A key is "used" when get or put is called on it.

Require O(1) average time for get and put.

Example:
  LRUCache(2)
  put(1, 10)  -> cache: {1=10}
  get(1)      -> 10
  put(2, 20)  -> cache: {1=10, 2=20}
  put(3, 30)  -> cache: {2=20, 3=30}, key 1 evicted
  get(2)      -> 20
  get(1)      -> -1

Constraints: 1 <= capacity <= 100, 0 <= key, value <= 1000

# region Hint 1
# Can you think of a data structure for storing key-value pairs?
# Maybe a hash-based structure with unique keys.
# endregion

# region Hint 2
# A hash map gives O(1) get/put. How do you track "least recently used"?
# What structure stores order?
# endregion

# region Hint 3
# Brute force: array list, iterate to erase/insert → O(n).
# What structure allows O(1) remove and reinsert?
# endregion

# region Hint 4
# A doubly-linked list lets you remove a node in O(1) given its address.
# How do you store those addresses for each key?
# endregion

# region Hint 5
# Doubly linked list: LRU at head, MRU at tail. On get/put, move node to tail.
# When full, evict from head. Use a hash map from key → node for O(1) lookup.
# endregion
'''


class LRUCache:
    def __init__(self, capacity: int):
        """Initialize LRU cache of given capacity."""
        pass

    def get(self, key: int) -> int:
        """Return value for key if exists, else -1."""
        pass

    def put(self, key: int, value: int) -> None:
        """Insert or update. Evict LRU if over capacity."""
        pass


# ========== TESTS ==========

def test_example():
    """Example from problem."""
    cache = LRUCache(2)
    cache.put(1, 10)
    assert_equal(cache.get(1), 10)
    cache.put(2, 20)
    cache.put(3, 30)
    assert_equal(cache.get(2), 20)
    assert_equal(cache.get(1), -1)


if __name__ == "__main__":
    run_tests()