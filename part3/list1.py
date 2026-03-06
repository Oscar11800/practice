from typing import List

# append the elements of arr2 to the end of arr1 and return the resulting list.
def append_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    pass

# remove the last n elements from the list and return the resulting list. If n is greater than the length of the list, it should return an empty list.
def pop_n(arr: List[int], n: int) -> List[int]:
    pass

# insert the element at the specified index in the list and return the resulting list. If the index is out of bounds, you should insert it at the end of the list.
def insert_at(arr: List[int], index: int, element: int) -> List[int]:
    pass


# do not modify below this line
print(append_elements([1, 2, 3], [4, 5, 6]))
print(append_elements([4, 3], [4, 5, 3]))

print(pop_n([1, 2, 3, 4, 5], 2))
print(pop_n([1, 2, 3, 4, 5], 6))
print(pop_n([1, 2, 3, 4, 5], 5))

print(insert_at([1, 2, 3, 4, 5], 2, 6))
print(insert_at([1, 2, 3, 4], 6, 5))
