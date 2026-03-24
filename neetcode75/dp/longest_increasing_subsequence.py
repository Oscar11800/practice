from neetcode75.test_runner import assert_equal, run_tests
from typing import List

"""
Longest Increasing Subsequence

Given an integer array nums, return the length of the longest strictly
increasing subsequence.

A subsequence is a sequence that can be derived from the given sequence by
deleting some or no elements without changing the relative order of the
remaining characters.

For example, "cat" is a subsequence of "crabt".

Example 1:
Input: nums = [9,1,4,2,3,3,7]
Output: 4
Explanation: The longest increasing subsequence is [1,2,3,7], length 4.

Example 2:
Input: nums = [0,3,1,3,2,3]
Output: 4

Constraints:
1 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        dp = [1] * (len(nums))
        rtn = 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j] + 1, dp[i])
            rtn = max(dp[i], rtn)

        return rtn


def test_example1():
    sol = Solution()
    assert_equal(sol.lengthOfLIS([9,1,4,2,3,3,7]), 4)


def test_example2():
    sol = Solution()
    assert_equal(sol.lengthOfLIS([0,3,1,3,2,3]), 4)


# Run: python3 -m neetcode75.dp.longest_increasing_subsequence
if __name__ == "__main__":
    run_tests()
