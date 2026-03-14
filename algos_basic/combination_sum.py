from typing import List
from test_runner import assert_equal, run_tests

'''
39. Combination Sum

You are given an array of distinct integers nums and a target integer target. Return a list
of all unique combinations of nums where the chosen numbers sum to target.

The same number may be chosen from nums an unlimited number of times. Two combinations are
the same if the frequency of each of the chosen numbers is the same, otherwise they are
different.

You may return the combinations in any order and the order of the numbers in each
combination can be in any order.

Example 1:
  Input: nums = [2,5,6,9], target = 9
  Output: [[2,2,5],[9]]
  Explanation: 2+2+5=9, 9=9.

Example 2:
  Input: nums = [3,4,5], target = 16
  Output: [[3,3,3,3,4],[3,3,5,5],[4,4,4,4],[3,4,4,5]]

Example 3:
  Input: nums = [3], target = 5
  Output: []

Constraints:
  All elements of nums are distinct.
  1 <= nums.length <= 20
  2 <= nums[i] <= 30
  2 <= target <= 30
'''


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Return all unique combinations that sum to target (reuse allowed).

        :param nums: Distinct integers to choose from.
        :param target: Target sum.
        :return: List of combinations (order does not matter).
        """
        pass


# ========== HELPERS ==========

def normalize_combinations(combs: List[List[int]]) -> List[List[int]]:
    """Sort combinations for comparison (problem allows any order)."""
    return sorted([sorted(c) for c in combs])


# ========== TESTS ==========

def test_example1():
    """Example 1: [2,5,6,9], target=9 -> [[2,2,5],[9]]."""
    sol = Solution()
    expected = [[2, 2, 5], [9]]
    assert_equal(
        normalize_combinations(sol.combinationSum([2, 5, 6, 9], 9)),
        normalize_combinations(expected),
    )


def test_example2():
    """Example 2: [3,4,5], target=16 -> [[3,3,3,3,4],[3,3,5,5],[4,4,4,4],[3,4,4,5]]."""
    sol = Solution()
    expected = [[3, 3, 3, 3, 4], [3, 3, 5, 5], [4, 4, 4, 4], [3, 4, 4, 5]]
    assert_equal(
        normalize_combinations(sol.combinationSum([3, 4, 5], 16)),
        normalize_combinations(expected),
    )


def test_example3():
    """Example 3: [3], target=5 -> []."""
    sol = Solution()
    assert_equal(sol.combinationSum([3], 5), [])


if __name__ == "__main__":
    run_tests()