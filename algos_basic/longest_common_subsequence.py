from test_runner import assert_equal, run_tests

'''
1143. Longest Common Subsequence

Given two strings text1 and text2, return the length of the longest common subsequence.
If none exists, return 0.

A subsequence can be formed by deleting characters without changing relative order.

Example:
  "cat" is a subsequence of "crabt"

Example 1:
  Input: text1 = "cat", text2 = "crabt"
  Output: 3
  Explanation: LCS is "cat"

Example 2:
  Input: text1 = "abcd", text2 = "abcd"
  Output: 4

Example 3:
  Input: text1 = "abcd", text2 = "efgh"
  Output: 0

Constraints:
  1 <= len(text1), len(text2) <= 1000
  text1, text2 contain lowercase English letters
'''


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Return length of the longest common subsequence of text1 and text2.

        :param text1: First string.
        :param text2: Second string.
        :return: Length of LCS.
        """
        pass


# ========== TESTS ==========

def test_example1():
    """Example 1 -> 3."""
    sol = Solution()
    assert_equal(sol.longestCommonSubsequence("cat", "crabt"), 3)


def test_example2():
    """Example 2 -> 4."""
    sol = Solution()
    assert_equal(sol.longestCommonSubsequence("abcd", "abcd"), 4)


def test_example3():
    """Example 3 -> 0."""
    sol = Solution()
    assert_equal(sol.longestCommonSubsequence("abcd", "efgh"), 0)


if __name__ == "__main__":
    run_tests()