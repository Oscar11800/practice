from email.policy import default
from test_runner import assert_equal, run_tests
from collections import Counter, defaultdict
'''
242. Valid Anagram

Given two strings s and t, return true if they are anagrams of each other,
otherwise return false.

An anagram contains the exact same characters as another string,
but the order can be different.

Example 1:
  Input: s = "racecar", t = "carrace"
  Output: true

Example 2:
  Input: s = "jar", t = "jam"
  Output: false

Constraints:
  s and t consist of lowercase English letters.
'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Return true if s and t are anagrams.

        :param s: First string.
        :param t: Second string.
        :return: True if same characters (any order), False otherwise.
        """
        if len(s) != len(t):
          return False
        
        freq = defaultdict(int)

        for c in s:
          freq[c] += 1
        
        for c in t:
          freq[c] -= 1

        for c in freq:
          if freq[c]:
            return False
        return True

# ========== TESTS ==========

def test_example1():
    """Example 1: racecar, carrace -> true."""
    sol = Solution()
    assert_equal(sol.isAnagram("racecar", "carrace"), True)


def test_example2():
    """Example 2: jar, jam -> false."""
    sol = Solution()
    assert_equal(sol.isAnagram("jar", "jam"), False)


if __name__ == "__main__":
    run_tests()