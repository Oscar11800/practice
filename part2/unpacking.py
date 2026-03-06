from math import prod
from typing import List, Tuple


# takes a list of 3 integers and returns the sum of the integers.
def sum_3_integers(triplet: List[int]) -> int:
    t1, t2, t3 = triplet
    return t1 + t2 + t3

# takes a list of 3 integers representing [width, height, depth] of a box and returns the volume of it.
def compute_volume(box_dimensions: Tuple[int, int, int]) -> int:
    w,h,d = box_dimensions
    return w * h * d
  

# do not modify below this line
print(sum_3_integers([1, 2, 3]))
print(sum_3_integers([4, 6, 2]))

print(compute_volume((1, 2, 3)))
print(compute_volume((3, 2, 1)))
print(compute_volume((3, 9, 7)))
