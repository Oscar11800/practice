from typing import List
from neetcode75.test_runner import assert_equal, run_tests

"""
Merge Intervals
Medium

Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

You may return the answer in any order.

Note: Intervals are non-overlapping if they have no common point. For example, [1, 2] and [3, 4] are non-overlapping, but [1, 2] and [2, 3] are overlapping.

Example 1:
Input: intervals = [[1,3],[1,5],[6,7]]
Output: [[1,5],[6,7]]

Example 2:
Input: intervals = [[1,2],[2,3]]
Output: [[1,3]]

Constraints:
1 <= intervals.length <= 1000
intervals[i].length == 2
0 <= start <= end <= 1000
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        raise NotImplementedError


def test_example1():
    sol = Solution()
    assert_equal(
        sol.merge([[1, 3], [1, 5], [6, 7]]), [[1, 5], [6, 7]]
    )


def test_example2():
    sol = Solution()
    assert_equal(sol.merge([[1, 2], [2, 3]]), [[1, 3]])


# Run: python3 -m neetcode75.intervals.merge_intervals
if __name__ == "__main__":
    run_tests()
