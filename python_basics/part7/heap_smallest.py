import heapq
from typing import List

# returns the smallest element in the list arr
def get_min_element(arr: List[int]) -> int:
    return heapq.nsmallest(1, arr)[0]

# returns the 4 smallest elements in the list arr in increasing order
def get_min_4_elements(arr: List[int]) -> List[int]:
    rtn = heapq.nsmallest(4, arr)
    return rtn

# returns the 2 smallest elements in the list arr in decreasing order
def get_min_2_elements(arr: List[int]) -> List[int]:
    rtn = heapq.nsmallest(2, arr)
    rtn.sort(reverse=True)
    return rtn


# do not modify below this line
print(get_min_element([1, 2, 3]))
print(get_min_element([3, 2, 1, 4, 6, 2]))
print(get_min_element([1, 9, 7, 3, 2, 1, 4, 6, 2]))

print(get_min_4_elements([1, 9, 7, 3, 2, 1, 4, 6, 2]))
print(get_min_4_elements([1, 9, 7, 2, 1, 3, 2, 1, 4, 6, 2, 1]))
print(get_min_4_elements([1, 9, 7, 2, 3, 2, 4, 6, 2]))

print(get_min_2_elements([1, 9, 7, 3, 2, 1, 4, 6, 2]))
print(get_min_2_elements([1, 9, 7, 2, 1, 3, 2, 1, 4, 6, 2, 1]))
print(get_min_2_elements([1, 9, 7, 2, 3, 2, 4, 6, 2]))

