from neetcode75.test_runner import assert_equal, run_tests

"""
Palindromic Substrings
Medium

Given a string s, return the number of substrings within s that are
palindromes.

A palindrome is a string that reads the same forward and backward.

Example 1:
Input: s = "abc"
Output: 3
Explanation: "a", "b", "c".

Example 2:
Input: s = "aaa"
Output: 6
Explanation: "a", "a", "a", "aa", "aa", "aaa". Note that different substrings
are counted as different palindromes even if the string contents are the same.

Constraints:
1 <= s.length <= 1000
s consists of lowercase English letters.
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        rtn = 0
        n = len(s)

        for i in range(n):
            left = right = i
            while left >= 0 and right < n and s[left] == s[right]:
                rtn += 1
                left -= 1
                right += 1
            left = i
            right = i+1
            while left >= 0 and right < n and s[left] == s[right]:
                rtn += 1
                left -= 1
                right += 1

        return rtn


def test_example1():
    sol = Solution()
    assert_equal(sol.countSubstrings("abc"), 3)


def test_example2():
    sol = Solution()
    assert_equal(sol.countSubstrings("aaa"), 6)


# Run: python3 -m neetcode75.dp.palindromic_substrings
if __name__ == "__main__":
    run_tests()
