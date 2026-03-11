from test_runner import assert_equal, run_tests
import math
'''
704. Binary Search

You are given an array of distinct integers nums, sorted in ascending order, and an
integer target.

Implement a function to search for target within nums. If it exists, return its index;
otherwise, return -1.

Your solution must run in O(log n) time.

Example 1:
  Input: nums = [-1,0,2,4,6,8], target = 4
  Output: 3

Example 2:
  Input: nums = [-1,0,2,4,6,8], target = 3
  Output: -1
'''


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        Binary search for target in sorted nums.

        :param nums: Sorted array of distinct integers.
        :param target: Value to search for.
        :return: Index of target, or -1 if not found.
        """
        l, r = 0, len(nums)-1
        m = math.ceil((l+r)/2)

        while l <= r:
            if nums[m] == target:
                return m
            elif target < nums[m]:
                r = m - 1
                m = math.ceil((l+r)/2)
            else:
                l = m + 1
                m = math.ceil((l+r)/2)
        return -1


# ========== TESTS ==========

def test_example1():
    """Example 1: target 4 at index 3."""
    sol = Solution()
    assert_equal(sol.search([-1, 0, 2, 4, 6, 8], 4), 3)


def test_example2():
    """Example 2: target 3 not found -> -1."""
    sol = Solution()
    assert_equal(sol.search([-1, 0, 2, 4, 6, 8], 3), -1)


if __name__ == "__main__":
    run_tests()
