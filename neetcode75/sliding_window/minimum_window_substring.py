from neetcode75.test_runner import assert_equal, run_tests

"""
Minimum Window Substring
Hard

Given two strings s and t, return the shortest substring of s such that every
character in t, including duplicates, is present in the substring. If such a
substring does not exist, return an empty string "".

You may assume that the correct output is always unique.

Example 1:
Input: s = "OUZODYXAZV", t = "XYZ"
Output: "YXAZ"
Explanation: "YXAZ" is the shortest substring that includes "X", "Y", and "Z"
from string t.

Example 2:
Input: s = "xyz", t = "xyz"
Output: "xyz"

Example 3:
Input: s = "x", t = "xy"
Output: ""

Constraints:
1 <= s.length <= 1000
1 <= t.length <= 1000
s and t consist of uppercase and lowercase English letters.
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        raise NotImplementedError


def test_example1():
    sol = Solution()
    assert_equal(sol.minWindow("OUZODYXAZV", "XYZ"), "YXAZ")


def test_example2():
    sol = Solution()
    assert_equal(sol.minWindow("xyz", "xyz"), "xyz")


def test_example3():
    sol = Solution()
    assert_equal(sol.minWindow("x", "xy"), "")


# Run: python3 -m neetcode75.sliding_window.minimum_window_substring
if __name__ == "__main__":
    run_tests()
