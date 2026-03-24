from neetcode75.test_runner import assert_equal, run_tests
from typing import List

"""
House Robber II

You are given an integer array nums where nums[i] represents the amount of
money the ith house has. The houses are arranged in a circle, i.e. the first
house and the last house are neighbors.

You are planning to rob money from the houses, but you cannot rob two adjacent
houses because the security system will automatically alert the police if two
adjacent houses were both broken into.

Return the maximum amount of money you can rob without alerting the police.

Example 1:
Input: nums = [3,4,3]
Output: 4
Explanation: You cannot rob nums[0] + nums[2] = 6 because nums[0] and nums[2]
are adjacent. The maximum you can rob is nums[1] = 4.

Example 2:
Input: nums = [2,9,8,3,6]
Output: 15
Explanation: The maximum you can rob is nums[1] + nums[4] = 15.

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 200
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp1 = [None] * (n-1)
        dp2 = [None] * (n-1)

        def dfs(house, dp, arr):
            if house >= (n-1):
                return 0
            if dp[house] != None:
                return dp[house]
            else:
                dp[house] = max(arr[house] + dfs(house+2, dp, arr), dfs(house+1, dp, arr))
            return dp[house]

        return max(dfs(0, dp1, nums[1:]), dfs(0, dp2, nums[:-1]))
        


def test_example1():
    sol = Solution()
    assert_equal(sol.rob([3,4,3]), 4)


def test_example2():
    sol = Solution()
    assert_equal(sol.rob([2,9,8,3,6]), 15)


# Run: python3 -m neetcode75.dp.house_robber_ii
if __name__ == "__main__":
    run_tests()
