from typing import List
from test_runner import assert_equal, run_tests

'''
217. Contains Duplicate

Given an integer array nums, return true if any value appears more than once
in the array, otherwise return false.

Example 1:
  Input: nums = [1, 2, 3, 3]
  Output: true

Example 2:
  Input: nums = [1, 2, 3, 4]
  Output: false
'''


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Return true if any value appears more than once.

        :param nums: Array of integers.
        :return: True if duplicates exist, False otherwise.
        """
        pass


# ========== TESTS ==========

def test_example1():
    """Example 1: [1,2,3,3] -> true."""
    sol = Solution()
    assert_equal(sol.containsDuplicate([1, 2, 3, 3]), True)


def test_example2():
    """Example 2: [1,2,3,4] -> false."""
    sol = Solution()
    assert_equal(sol.containsDuplicate([1, 2, 3, 4]), False)


if __name__ == "__main__":
    run_tests()