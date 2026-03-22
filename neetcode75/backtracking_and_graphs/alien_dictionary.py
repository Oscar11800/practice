from neetcode75.test_runner import assert_equal, run_tests
from typing import List

"""
Alien Dictionary
Hard

There is a foreign language which uses the latin alphabet, but the order among
letters is not "a", "b", "c" ... "z" as in English.

You receive a list of non-empty strings words from the dictionary, where the
words are sorted lexicographically based on the rules of this new language.

Derive the order of letters in this language. If the order is invalid, return
an empty string. If there are multiple valid orders of letters, return any of
them.

A string a is lexicographically smaller than b if either:
- The first letter where they differ is smaller in a than in b.
- a is a prefix of b and a.length < b.length.

Example 1:
Input: ["z","o"]
Output: "zo"
Explanation: From "z" and "o", we know 'z' < 'o', so return "zo".

Example 2:
Input: ["hrn","hrf","er","enn","rfnn"]
Output: "hernf"
Explanation:
from "hrn" and "hrf", we know 'n' < 'f'
from "hrf" and "er", we know 'h' < 'e'
from "er" and "enn", we know 'r' < 'n'
from "enn" and "rfnn", we know 'e' < 'r'
so one possible solution is "hernf"

Constraints:
The input words will contain characters only from lowercase 'a' to 'z'
1 <= words.length <= 100
1 <= words[i].length <= 100
"""


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        raise NotImplementedError


def test_example1():
    sol = Solution()
    assert_equal(sol.foreignDictionary(["z","o"]), "zo")


def test_example2():
    sol = Solution()
    assert_equal(sol.foreignDictionary(["hrn","hrf","er","enn","rfnn"]), "hernf")


# Run: python3 -m neetcode75.backtracking_and_graphs.alien_dictionary
if __name__ == "__main__":
    run_tests()
