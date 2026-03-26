from typing import List
from neetcode75.test_runner import assert_equal, run_tests

"""
Meeting Rooms II
Medium

Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), find the minimum number of rooms required to schedule all meetings without any conflicts.

Note: (0,8),(8,10) is NOT considered a conflict at 8.

Example 1:
Input: intervals = [(0,40),(5,10),(15,20)]
Output: 2

Example 2:
Input: intervals = [(4,9)]
Output: 1

Constraints:
0 <= intervals.length <= 500
0 <= intervals[i].start < intervals[i].end <= 1,000,000
"""


class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        raise NotImplementedError


def test_example1():
    sol = Solution()
    assert_equal(
        sol.minMeetingRooms(
            [Interval(0, 40), Interval(5, 10), Interval(15, 20)]
        ),
        2,
    )


def test_example2():
    sol = Solution()
    assert_equal(sol.minMeetingRooms([Interval(4, 9)]), 1)


# Run: python3 -m neetcode75.intervals.meeting_rooms_ii
if __name__ == "__main__":
    run_tests()
