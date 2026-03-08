from typing import List
from sortedcontainers import SortedDict

# take a sorted dictionary and a list of keys and remove the key-value pairs associated with those keys from the dictionary. 
# Return the modified sorted dictionary.
def remove_keys(sorted_dict: SortedDict[str, int], keys: List[str]) -> SortedDict[str, int]:
    for key in keys:
        sorted_dict.pop(key)
    return sorted_dict

# take a sorted dictionary and a target key and return a list of values associated with keys
# that come before the target key in sorted order.
def get_values_before_target(sorted_dict: SortedDict[str, int], target: str) -> List[int]:
    l = []
    for key, val in sorted_dict.items():
        if key == target:
            break
        else:
            l.append(val)
    return l


# do not modify below this line
print(remove_keys(SortedDict({'Alice': 25, 'Bob': 30, 'Charlie': 35}), ['Bob']))
print(remove_keys(SortedDict({'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40}), ['Bob', 'David']))
print(remove_keys(SortedDict({'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40, 'Eve': 45}), ['Alice', 'Eve']))

print(get_values_before_target(SortedDict({'Alice': 25, 'Bob': 30, 'Charlie': 35}), 'Bob'))
print(get_values_before_target(SortedDict({'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40}), 'David'))
print(get_values_before_target(SortedDict({'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40}), 'Charlie'))
print(get_values_before_target(SortedDict({'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40}), 'Bob'))
print(get_values_before_target(SortedDict({'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40}), 'Alice'))
