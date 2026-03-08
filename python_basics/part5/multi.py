from typing import List

def find_max_in_list(arr: List[int]) -> List[int]:
    rtn = float('-inf')
    for ele in arr:
        rtn = max(rtn, ele)
    return rtn

# takes a 2D list of integers and returns a list of the maximum element in each sublist. 
# The returned list should contain the maximum element from each sublist in the order they appear in the input list.
def find_max_in_each_list(nested_arr: List[List[int]]) -> List[int]:
    return (list(map(max, nested_arr)))
    return [max(sublist) for sublist in nested_arr]


# do not modify below this line
print(find_max_in_each_list([[1, 2], [3, 4, 2]]))
print(find_max_in_each_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(find_max_in_each_list([[5, 6, 2, 8], [9], [9, 10], [11, 10, 11]]))
