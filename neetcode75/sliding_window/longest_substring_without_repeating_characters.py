from neetcode75.test_runner import assert_equal, run_tests

"""
Longest Substring Without Repeating Characters
Medium

Given a string s, find the length of the longest substring without duplicate
characters.

A substring is a contiguous sequence of characters within a string.

Example 1:
Input: s = "zxyzxyz"
Output: 3
Explanation: The string "xyz" is the longest without duplicate characters.

Example 2:
Input: s = "xxxx"
Output: 1

Constraints:
0 <= s.length <= 1000
s may consist of printable ASCII characters.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        raise NotImplementedError


def test_example1():
    sol = Solution()
    assert_equal(sol.lengthOfLongestSubstring("zxyzxyz"), 3)


def test_example2():
    sol = Solution()
    assert_equal(sol.lengthOfLongestSubstring("xxxx"), 1)


def test_empty_string():
    sol = Solution()
    assert_equal(sol.lengthOfLongestSubstring(""), 0)


# Run: python3 -m neetcode75.sliding_window.longest_substring_without_repeating_characters
if __name__ == "__main__":
    run_tests()
