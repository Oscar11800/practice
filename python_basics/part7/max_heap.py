import heapq
from typing import List

# takes a list of integers and returns the integers in reverse sorted order. 
# You should use the max heap technique described above to achieve this. 
# The list of integers given is not necessarily a heap.
def get_reverse_sorted(nums: List[int]) -> List[int]:
    max_heap = []
    for num in nums:
        heapq.heappush(max_heap, -num)
    return [-heapq.heappop(max_heap) for _ in range(len(nums))]

# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
