from typing import List, Dict

# takes a list of integers and returns a dictionary where the keys are the elements of the list 
# and the values are the indices of those elements in the list. You can assume that all elements in the list are unique.
def num_to_index(nums: List[int]) -> Dict[int, int]:
    return {num : i for i,  num in enumerate(nums)}


# do not modify below this line
print(num_to_index([1, 2, 3, 4, 5, 6, 7, 8]))
print(num_to_index([8, 7, 6, 5, 4, 3, 2, 1]))
print(num_to_index([0, 3, 2, 4, 5, 1]))
