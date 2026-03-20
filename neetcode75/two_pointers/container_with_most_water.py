from typing import List
from neetcode75.test_runner import assert_equal, run_tests

"""
Container With Most Water

You are given an integer array heights where heights[i] represents the height of
the ith bar.

You may choose any two bars to form a container. Return the maximum amount of
water a container can store.

Example 1:

Input: height = [1,7,2,5,4,7,3,6]

Output: 36
Example 2:

Input: height = [2,2,2]

Output: 4
Constraints:

2 <= height.length <= 1000
0 <= height[i] <= 1000
"""


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left, right = 0, len(heights)-1
        while left < right:
            area = (right-left) * (min(heights[left], heights[right]))
            max_area = max(area, max_area)
            if heights[left] < heights[right]:
                left += 1
            elif heights[left] == heights[right]:
                left += 1
                right -= 1
            else:
                right -= 1
        return max_area


def test_example1():
    sol = Solution()
    assert_equal(sol.maxArea([1, 7, 2, 5, 4, 7, 3, 6]), 36)


def test_example2():
    sol = Solution()
    assert_equal(sol.maxArea([2, 2, 2]), 4)


if __name__ == "__main__":
    run_tests()
