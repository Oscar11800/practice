import heapq
from typing import List

# pushes the integer value onto the heap heap. 
# The heap should be a min heap, meaning that the element with the smallest priority should be at index 0. 
# After pushing the element, return the element with the smallest priority.
def heap_push(heap: List[int], value: int) -> int:
    heapq.heappush(heap, value)
    return heap[0]


# do not modify below this line
print(heap_push([1, 2, 3], 4))
print(heap_push([1, 2, 3], 0))
print(heap_push([1, 2, 3], 2))
print(heap_push([4, 6, 7, 8, 12, 9, 10], 2))
print(heap_push([4, 6, 7, 8, 12, 9, 10], 5))
