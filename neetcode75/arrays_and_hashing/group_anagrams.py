from typing import List
from test_runner import assert_equal, run_tests

'''
49. Group Anagrams

Given an array of strings strs, group all anagrams into sublists.
You may return groups in any order.

An anagram contains the exact same characters as another string,
but with possibly different order.

Example 1:
  Input: strs = ["act","pots","tops","cat","stop","hat"]
  Output: [["hat"],["act","cat"],["stop","pots","tops"]]

Example 2:
  Input: strs = ["x"]
  Output: [["x"]]

Example 3:
  Input: strs = [""]
  Output: [[""]]

Constraints:
  1 <= strs.length <= 1000
  0 <= strs[i].length <= 100
  strs[i] contains lowercase English letters
'''


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Group anagrams together.

        :param strs: List of input strings.
        :return: List of anagram groups (order not important).
        """
        rtn = []
        base = ord('a')
        matchmap = {}

        for s in strs:
            charmap = {i : 0 for i in range(26)}
            for c in s:
                charmap[ord(c) - base] += 1
            key = tuple(charmap.values())
            if key in matchmap:
                rtn[matchmap[key]].append(s)
            else:
                matchmap[key] = len(rtn)
                rtn.append([s])
        return rtn


# ========== HELPERS ==========

def normalize_groups(groups: List[List[str]]) -> List[List[str]]:
    """
    Normalize nested groups for comparison:
    - sort words within each group
    - sort groups by (len, lexicographic tuple)
    """
    normalized = [sorted(group) for group in groups]
    normalized.sort(key=lambda g: (len(g), tuple(g)))
    return normalized


# ========== TESTS ==========

def test_example1():
    """Example 1."""
    sol = Solution()
    inp = ["act", "pots", "tops", "cat", "stop", "hat"]
    expected = [["hat"], ["act", "cat"], ["stop", "pots", "tops"]]
    assert_equal(normalize_groups(sol.groupAnagrams(inp)), normalize_groups(expected))


def test_example2():
    """Example 2."""
    sol = Solution()
    assert_equal(normalize_groups(sol.groupAnagrams(["x"])), normalize_groups([["x"]]))


def test_example3():
    """Example 3."""
    sol = Solution()
    assert_equal(normalize_groups(sol.groupAnagrams([""])), normalize_groups([[""]]))


if __name__ == "__main__":
    run_tests()