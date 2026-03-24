from neetcode75.test_runner import assert_equal, run_tests

"""
Decode Ways
Medium

A string consisting of uppercase english characters can be encoded to a number
using the following mapping:
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"

To decode a message, digits must be grouped and then mapped back into letters
using the reverse of the mapping above. There may be multiple ways to decode
a message.

The grouping (1 01 2) is invalid because "01" cannot be mapped into a letter
since it contains a leading zero.

Given a string s containing only digits, return the number of ways to decode
it. You can assume the answer fits in a 32-bit integer.

Example 1:
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: s = "01"
Output: 0
Explanation: "01" cannot be decoded because "01" cannot be mapped into a letter.

Constraints:
1 <= s.length <= 100
s consists of digits.
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        raise NotImplementedError


def test_example1():
    sol = Solution()
    assert_equal(sol.numDecodings("12"), 2)


def test_example2():
    sol = Solution()
    assert_equal(sol.numDecodings("01"), 0)


# Run: python3 -m neetcode75.dp.decode_ways
if __name__ == "__main__":
    run_tests()
