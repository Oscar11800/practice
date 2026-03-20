from collections import defaultdict
import heapq
from typing import List
from neetcode75.test_runner import assert_equal, run_tests

'''
347. Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements.

The answer is guaranteed to be unique.
You may return the output in any order.

Example 1:
  Input: nums = [1,2,2,3,3,3], k = 2
  Output: [2,3]

Example 2:
  Input: nums = [7,7], k = 1
  Output: [7]

Constraints:
  1 <= nums.length <= 10^4
  -1000 <= nums[i] <= 1000
  1 <= k <= number of distinct elements in nums
'''


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Return the k most frequent elements.

        :param nums: List of integers.
        :param k: Number of top frequent elements to return.
        :return: List of k most frequent elements (any order).
        """
        occurences = defaultdict(int)
        # count occurences
        for num in nums:
            occurences[num] += 1
        heap = [(-val, key) for key, val in occurences.items()]
        heapq.heapify(heap)
        rtn = []

        for _ in range(k):
            rtn.append(heapq.heappop(heap)[1])
        return rtn



# ========== HELPERS ==========

def normalize(ans: List[int]) -> List[int]:
    """Sort output for deterministic test comparison."""
    return sorted(ans)


# ========== TESTS ==========

def test_example1():
    """Example 1 -> [2,3] (any order)."""
    sol = Solution()
    assert_equal(normalize(sol.topKFrequent([1, 2, 2, 3, 3, 3], 2)), normalize([2, 3]))


def test_example2():
    """Example 2 -> [7]."""
    sol = Solution()
    assert_equal(normalize(sol.topKFrequent([7, 7], 1)), normalize([7]))


if __name__ == "__main__":
    run_tests()