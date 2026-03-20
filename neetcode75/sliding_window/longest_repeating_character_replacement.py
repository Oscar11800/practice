from neetcode75.test_runner import assert_equal, run_tests

"""
Longest Repeating Character Replacement
Medium

You are given a string s consisting of only uppercase english characters and an
integer k. You can choose up to k characters of the string and replace them
with any other uppercase English character.

After performing at most k replacements, return the length of the longest
substring which contains only one distinct character.

Example 1:
Input: s = "XYYX", k = 2
Output: 4
Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.

Example 2:
Input: s = "AAABABB", k = 1
Output: 5

Constraints:
1 <= s.length <= 1000
0 <= k <= s.length
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        raise NotImplementedError


def test_example1():
    sol = Solution()
    assert_equal(sol.characterReplacement("XYYX", 2), 4)


def test_example2():
    sol = Solution()
    assert_equal(sol.characterReplacement("AAABABB", 1), 5)


def test_no_replacement():
    sol = Solution()
    assert_equal(sol.characterReplacement("ABCD", 0), 1)


# Run: python3 -m neetcode75.sliding_window.longest_repeating_character_replacement
if __name__ == "__main__":
    run_tests()
