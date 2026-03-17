from typing import List
from test_runner import assert_equal, run_tests

'''
1. Two Sum

Given an array of integers nums and an integer target, return the indices i and j
such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one valid answer.
Return the answer with the smaller index first.

Example 1:
  Input: nums = [3,4,5,6], target = 7
  Output: [0,1]
  Explanation: nums[0] + nums[1] == 7

Example 2:
  Input: nums = [4,5,6], target = 10
  Output: [0,2]

Example 3:
  Input: nums = [5,5], target = 10
  Output: [0,1]

Constraints:
  2 <= nums.length <= 1000
  -10^7 <= nums[i], target <= 10^7
  Exactly one valid answer exists.
'''


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Return indices of two numbers that add up to target.

        :param nums: Array of integers.
        :param target: Target sum.
        :return: [i, j] where nums[i] + nums[j] == target, i < j.
        """
        hashmap = {}
        for idx, num in enumerate(nums):
          diff = target - num
          if diff in hashmap:
            return [hashmap[diff], idx]
          else:
            hashmap[num] = idx
        return [-1, -1]


# ========== TESTS ==========

def test_example1():
    """Example 1: [3,4,5,6], target=7 -> [0,1]."""
    sol = Solution()
    assert_equal(sol.twoSum([3, 4, 5, 6], 7), [0, 1])


def test_example2():
    """Example 2: [4,5,6], target=10 -> [0,2]."""
    sol = Solution()
    assert_equal(sol.twoSum([4, 5, 6], 10), [0, 2])


def test_example3():
    """Example 3: [5,5], target=10 -> [0,1]."""
    sol = Solution()
    assert_equal(sol.twoSum([5, 5], 10), [0, 1])


if __name__ == "__main__":
    run_tests()