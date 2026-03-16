from typing import List
from test_runner import assert_equal, run_tests
import heapq
'''
703. Kth Largest Element in a Stream

Design a class to find the kth largest integer in a stream of values, including duplicates.
E.g. the 2nd largest from [1, 2, 3, 3] is 3. The stream is not necessarily sorted.

Implement the following methods:
- __init__(k, nums): Initialize with k and the initial stream nums.
- add(val): Add val to the stream and return the kth largest integer.

Example:
  KthLargest(3, [1, 2, 3, 3])
  add(3) -> 3   (stream: [1,2,3,3,3], 3rd largest = 3)
  add(5) -> 3   (stream: [1,2,3,3,3,5], 3rd largest = 3)
  add(6) -> 3
  add(7) -> 5
  add(8) -> 6

Constraints:
  1 <= k <= 1000
  0 <= nums.length <= 1000
  -1000 <= nums[i], val <= 1000
  At least k integers in stream when searching.
'''


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        """
        Initialize with k and initial stream nums.
        """
        self.k = k
        self.nums = []
        for num in nums:
            if len(self.nums) == k:
                if num > self.nums[0]:
                    heapq.heappop(self.nums)
                    heapq.heappush(self.nums, num)
            else:
                heapq.heappush(self.nums, num)

    def add(self, val: int) -> int:
        """
        Add val to the stream and return the kth largest integer.
        """
        if len(self.nums) == self.k:
            if val >= self.nums[0]:
                heapq.heappop(self.nums)
                heapq.heappush(self.nums, val)
        else:
            heapq.heappush(self.nums, val)
        return self.nums[0]


# ========== TESTS ==========

def test_example():
    """Example from problem."""
    obj = KthLargest(3, [1, 2, 3, 3])
    assert_equal(obj.add(3), 3)
    assert_equal(obj.add(5), 3)
    assert_equal(obj.add(6), 3)
    assert_equal(obj.add(7), 5)
    assert_equal(obj.add(8), 6)


if __name__ == "__main__":
    run_tests()