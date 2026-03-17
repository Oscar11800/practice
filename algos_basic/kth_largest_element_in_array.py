from typing import List
from test_runner import assert_equal, run_tests
import heapq
'''
215. Kth Largest Element in an Array

Given an unsorted array of integers nums and an integer k, return the kth largest
element in the array.

By kth largest we mean the kth largest in sorted order, not the kth distinct element.
E.g. in [2,3,1,1,5,5,4], the sorted order is [5,5,4,3,2,1,1], so 3rd largest is 4.

Follow-up: Can you solve it without sorting?

Example 1:
  Input: nums = [2,3,1,5,4], k = 2
  Output: 4

Example 2:
  Input: nums = [2,3,1,1,5,5,4], k = 3
  Output: 4

Constraints:
  1 <= k <= nums.length <= 10000
  -1000 <= nums[i] <= 1000
'''


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Return the kth largest element in nums (sorted order, not distinct).

        :param nums: Unsorted array of integers.
        :param k: 1-indexed position (1 = largest).
        :return: The kth largest value.
        """
        nums = [-num for num in nums]
        heapq.heapify(nums)
        for _ in range(k-1):
            heapq.heappop(nums)
        return -heapq.heappop(nums)


# ========== TESTS ==========

def test_example1():
    """Example 1: [2,3,1,5,4], k=2 -> 4."""
    sol = Solution()
    assert_equal(sol.findKthLargest([2, 3, 1, 5, 4], 2), 4)


def test_example2():
    """Example 2: [2,3,1,1,5,5,4], k=3 -> 4."""
    sol = Solution()
    assert_equal(sol.findKthLargest([2, 3, 1, 1, 5, 5, 4], 3), 4)


if __name__ == "__main__":
    run_tests()