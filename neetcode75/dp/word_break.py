from neetcode75.test_runner import assert_equal, run_tests
from typing import List

"""
Word Break
Medium

Given a string s and a dictionary of strings wordDict, return true if s can
be segmented into a space-separated sequence of dictionary words.

You are allowed to reuse words in the dictionary an unlimited number of times.
You may assume all dictionary words are unique.

Example 1:
Input: s = "neetcode", wordDict = ["neet","code"]
Output: true
Explanation: "neetcode" can be split into "neet" and "code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen","ape"]
Output: true
Explanation: "applepenapple" can be split into "apple", "pen", "apple".

Example 3:
Input: s = "catsincars", wordDict = ["cats","cat","sin","in","car"]
Output: false

Constraints:
1 <= s.length <= 200
1 <= wordDict.length <= 100
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        raise NotImplementedError


def test_example1():
    sol = Solution()
    assert_equal(sol.wordBreak("neetcode", ["neet","code"]), True)


def test_example2():
    sol = Solution()
    assert_equal(sol.wordBreak("applepenapple", ["apple","pen","ape"]), True)


def test_example3():
    sol = Solution()
    assert_equal(sol.wordBreak("catsincars", ["cats","cat","sin","in","car"]), False)


# Run: python3 -m neetcode75.dp.word_break
if __name__ == "__main__":
    run_tests()
