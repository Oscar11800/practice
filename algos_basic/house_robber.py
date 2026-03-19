from typing import List
from test_runner import assert_equal, run_tests

'''
198. House Robber

You are given an integer array nums where nums[i] is the money in the ith house.
Houses are in a line, so adjacent houses cannot both be robbed.

Return the maximum money you can rob without robbing adjacent houses.

Example 1:
  Input: nums = [1,1,3,3]
  Output: 4
  Explanation: rob houses 0 and 2 -> 1 + 3 = 4

Example 2:
  Input: nums = [2,9,8,3,6]
  Output: 16
  Explanation: rob houses 0,2,4 -> 2 + 8 + 6 = 16

Constraints:
  1 <= nums.length <= 100
  0 <= nums[i] <= 100
'''


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Return maximum amount that can be robbed without taking adjacent houses.

        :param nums: Money in each house.
        :return: Maximum robbable amount.
        """
        best_sum = {}
        n = len(nums)
        def dfs(index):
            if index >= n:
                return 0
            if index in best_sum:
                return best_sum[index]
            else:
                best_sum[index] = max(dfs(index + 1), nums[index] + dfs(index + 2))
            return best_sum[index]
        return dfs(0)



# ========== TESTS ==========

def test_example1():
    """Example 1 -> 4."""
    sol = Solution()
    assert_equal(sol.rob([1, 1, 3, 3]), 4)


def test_example2():
    """Example 2 -> 16."""
    sol = Solution()
    assert_equal(sol.rob([2, 9, 8, 3, 6]), 16)


if __name__ == "__main__":
    run_tests()