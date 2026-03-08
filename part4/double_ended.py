from typing import List, Deque
from collections import deque

#  takes a list of integers arr and an integer k. It should convert the list into a deque.
#  And next, rotate the values in the list to the right by k steps and return the resulting deque.
def rotate_list(arr: List[int], k: int) -> Deque[int]:
    rot = deque(arr)
    for i in range(k):
        rot.appendleft(rot.pop())
    return rot


# do not modify below this line
print(rotate_list([1, 2, 3, 4, 5], 0))
print(rotate_list([1, 2, 3, 4, 5], 1))
print(rotate_list([1, 2, 3, 4, 5], 2))
print(rotate_list([1, 2, 3, 4, 5], 3))
print(rotate_list([1, 2, 3, 4, 5], 4))
print(rotate_list([1, 2, 3, 4, 5], 5))
