from typing import List, Dict

# takes two lists, keys and values, and returns a hash map where the keys are the elements of the keys list 
# and the values are the elements of the values list.
def build_hash_map(keys: List[str], values: List[int]) -> Dict[str, int]:
    hmap = {}
    for key, val in zip(keys, values):
        hmap[key] = val
    return hmap

# takes a hash map and a list of keys and returns a list of the values associated with those keys.
def get_values(hash_map: Dict[str, int], keys: List[str]) -> List[int]:
    l = []
    for key in keys:
        l.append(hash_map[key])
    return l


# do not modify below this line
print(build_hash_map(["Alice", "Bob", "Charlie"], [90, 80, 70]))
print(build_hash_map(["Jane", "Carol", "Charlie"], [25, 100, 60]))
print(build_hash_map(["Doug", "Bob", "Tommy"], [80, 90, 100]))

print(get_values({"Alice": 90, "Bob": 80, "Charlie": 70}, ["Alice", "Bob", "Charlie"]))
print(get_values({"Jane": 25, "Charlie": 60, "Carol": 100, }, ["Jane", "Carol"]))
print(get_values({"X": 205, "Y": 78, "Z": 100}, ["Y"]))
