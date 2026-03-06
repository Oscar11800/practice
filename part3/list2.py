from typing import List

# append the elements of arr2 to the end of arr1 and return the resulting list. Yes, this is the same function from the previous lesson.
def append_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    pass
  
# remove all elements of arr2 from arr1 and return the resulting list.
# If any of the elements in arr2 are not in arr1, then skip them.
def remove_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    pass


# do not modify below this line
print(append_elements([1, 2, 3], [4, 5, 6]))
print(append_elements([4, 3], [4, 5, 3]))

print(remove_elements([1, 2, 3, 4, 5], [2, 4, 6]))
print(remove_elements([1, 2, 3, 4, 5], [2, 3, 4, 5, 5]))
print(remove_elements([1, 7, 2, 3, 4, 5], [6, 7, 8, 2]))
