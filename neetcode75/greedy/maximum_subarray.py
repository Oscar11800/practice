from typing import List
from neetcode75.test_runner import assert_equal, run_tests

"""
Maximum Subarray
Medium

Given an array of integers nums, find the subarray with the largest sum and return the sum.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [2,-3,4,-2,2,1,-1,4]
Output: 8
Explanation: The subarray [4,-2,2,1,-1,4] has the largest sum 8.

Example 2:
Input: nums = [-1]
Output: -1

Constraints:
1 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        rtn = float('-inf')
        curr_sum = 0
        for num in nums:
            curr_sum += num
            rtn = max(curr_sum, rtn)
            if curr_sum < 0:
                curr_sum = 0
        return rtn


def test_example1():
    sol = Solution()
    assert_equal(sol.maxSubArray([2, -3, 4, -2, 2, 1, -1, 4]), 8)


def test_example2():
    sol = Solution()
    assert_equal(sol.maxSubArray([-1]), -1)


# Run: python3 -m neetcode75.greedy.maximum_subarray
if __name__ == "__main__":
    run_tests()
