from typing import List
from neetcode75.test_runner import assert_equal, run_tests

"""
Non-overlapping Intervals
Medium

Given an array of intervals intervals where intervals[i] = [start_i, end_i], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note: Intervals are non-overlapping even if they have a common point. For example, [1, 2] and [2, 3] are non-overlapping.

Example 1:
Input: intervals = [[1,2],[2,4],[1,4]]
Output: 1
Explanation: After [1,4] is removed, the rest of the intervals are non-overlapping.

Example 2:
Input: intervals = [[1,2],[2,4]]
Output: 0

Constraints:
1 <= intervals.length <= 1000
intervals[i].length == 2
-50000 <= starti < endi <= 50000
"""


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        raise NotImplementedError


def test_example1():
    sol = Solution()
    assert_equal(
        sol.eraseOverlapIntervals([[1, 2], [2, 4], [1, 4]]), 1
    )


def test_example2():
    sol = Solution()
    assert_equal(sol.eraseOverlapIntervals([[1, 2], [2, 4]]), 0)


# Run: python3 -m neetcode75.intervals.non_overlapping_intervals
if __name__ == "__main__":
    run_tests()
