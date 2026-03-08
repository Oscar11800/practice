from collections import defaultdict
from typing import Any, List, Dict

#  takes a string and returns a dictionary where the keys are the characters in the string and 
# the values are the number of times each character appears in the string
def count_chars(s: str) -> Dict[str, int]:
    dick = defaultdict(int)
    for c in s:
        dick[c] += 1
    return dick

#  takes a list of lists of integers and returns a dictionary where the keys are the first element of each list
#  and the values are the rest of the elements in the list.
def nested_list_to_dict(nums: List[List[int]]) -> Dict[int, List[int]]:
    dick = defaultdict(list)
    for sublist in nums:
        dick[sublist[0]] += sublist[1:]
    return dick


# do not modify below this line
print(count_chars("hello"))
print(count_chars("helloworld"))
print(count_chars("areallylongstringwhyareyoureadingthishahalol"))

print(nested_list_to_dict([[1, 2, 3], [4, 5, 6], [1, 4]]))
print(nested_list_to_dict([[1, 2, 3, 4], [4, 5, 6, 7], [1, 4, 5, 6]]))
print(nested_list_to_dict([[5, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]))
print(nested_list_to_dict([[3, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8]]))
