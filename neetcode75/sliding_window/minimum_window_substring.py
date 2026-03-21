from neetcode75.test_runner import assert_equal, run_tests
from collections import Counter
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
        if s == "" or t == "":
            return ""
        if len(s) < len(t):
            return ""

        freqt = Counter(t)
        window = Counter()

        have = 0
        need = len(freqt)

        left, right = 0, 0
        n = len(s)
        rtn_str = ""

        for right in range(n):
            if s[right] in freqt.keys():
                window[s[right]] += 1
                if window[s[right]] == freqt[s[right]]:
                    have += 1
            while have == need:
                if (right - left + 1) < len(rtn_str) or rtn_str == "":
                    rtn_str = s[left:right+1]
                if s[left] in freqt.keys():
                    window.subtract(s[left])
                    if window[s[left]] < freqt[s[left]]:
                        have -= 1
                left += 1
        return rtn_str



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
