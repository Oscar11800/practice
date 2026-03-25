from neetcode75.test_runner import assert_equal, run_tests
from typing import List

"""
Maximum Product Subarray
Medium

Given an integer array nums, find a subarray that has the largest product
within the array and return it.

A subarray is a contiguous non-empty sequence of elements within an array.

You can assume the output will fit into a 32-bit integer.

Example 1:
Input: nums = [1,2,-3,4]
Output: 4

Example 2:
Input: nums = [-2,-1]
Output: 2

Constraints:
1 <= nums.length <= 1000
-10 <= nums[i] <= 10
"""


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        rtn = nums[0]
        max_product = 1
        min_product = 1
        for i in range(len(nums)):
            temp = max_product
            max_product = max(nums[i], nums[i] * max_product, nums[i] * min_product)
            min_product = min(nums[i], nums[i] * temp, nums[i] * min_product)
            rtn = max(max_product, rtn)

        return rtn

def test_example1():
    sol = Solution()
    assert_equal(sol.maxProduct([1,2,-3,4]), 4)


def test_example2():
    sol = Solution()
    assert_equal(sol.maxProduct([-2,-1]), 2)


# Run: python3 -m neetcode75.dp.maximum_product_subarray
if __name__ == "__main__":
    run_tests()
