from neetcode75.test_runner import assert_equal, run_tests
from typing import List

"""
Word Search
Medium

Given a 2-D grid of characters board and a string word, return true if the
word is present in the grid, otherwise return false.

For the word to be present it must be possible to form it with a path in the
board with horizontally or vertically neighboring cells. The same cell may not
be used more than once in a word.

Example 1:
Input:
board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
],
word = "CAT"
Output: true

Example 2:
Input:
board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
],
word = "BAT"
Output: false

Constraints:
1 <= board.length, board[i].length <= 5
1 <= word.length <= 10
board and word consists of only lowercase and uppercase English letters
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        raise NotImplementedError


def test_example1():
    sol = Solution()
    board = [
        ["A","B","C","D"],
        ["S","A","A","T"],
        ["A","C","A","E"]
    ]
    assert_equal(sol.exist(board, "CAT"), True)


def test_example2():
    sol = Solution()
    board = [
        ["A","B","C","D"],
        ["S","A","A","T"],
        ["A","C","A","E"]
    ]
    assert_equal(sol.exist(board, "BAT"), False)


# Run: python3 -m neetcode75.backtracking_and_graphs.word_search
if __name__ == "__main__":
    run_tests()
