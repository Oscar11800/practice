from typing import List
from neetcode75.test_runner import assert_equal, run_tests

"""
Meeting Rooms
Easy

Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), determine if a person could add all meetings to their schedule without any conflicts.

Note: (0,8),(8,10) is not considered a conflict at 8

Example 1:
Input: intervals = [(0,30),(5,10),(15,20)]
Output: false

Example 2:
Input: intervals = [(5,8),(9,15)]
Output: true

Constraints:
0 <= intervals.length <= 500
0 <= intervals[i].start < intervals[i].end <= 1,000,000
"""


class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        raise NotImplementedError


def test_example1():
    sol = Solution()
    assert_equal(
        sol.canAttendMeetings(
            [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
        ),
        False,
    )


def test_example2():
    sol = Solution()
    assert_equal(
        sol.canAttendMeetings([Interval(5, 8), Interval(9, 15)]), True
    )


# Run: python3 -m neetcode75.intervals.meeting_rooms
if __name__ == "__main__":
    run_tests()
