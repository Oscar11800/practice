from typing import List
from test_runner import assert_equal, run_tests

'''
78. Subsets

Given an array nums of unique integers, return all possible subsets of nums.

The solution set must not contain duplicate subsets. You may return the solution in any order.

Example 1:
  Input: nums = [1,2,3]
  Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
  Input: nums = [7]
  Output: [[],[7]]

Constraints:
  1 <= nums.length <= 10
  -10 <= nums[i] <= 10
'''


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Return all possible subsets of nums (power set).

        :param nums: List of unique integers.
        :return: List of all subsets (order does not matter).
        """
        pass


# ========== HELPERS ==========

def normalize_subsets(subsets: List[List[int]]) -> List[List[int]]:
    """Sort subsets for comparison (problem allows any order)."""
    return sorted([sorted(s) for s in subsets])


# ========== TESTS ==========

def test_example1():
    """Example 1: [1,2,3] -> [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]."""
    sol = Solution()
    expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    assert_equal(normalize_subsets(sol.subsets([1, 2, 3])), normalize_subsets(expected))


def test_example2():
    """Example 2: [7] -> [[],[7]]."""
    sol = Solution()
    expected = [[], [7]]
    assert_equal(normalize_subsets(sol.subsets([7])), normalize_subsets(expected))


if __name__ == "__main__":
    run_tests()