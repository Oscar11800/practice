from typing import List
from test_runner import assert_equal, run_tests

'''
1091. Shortest Path in Binary Matrix

Given an n x n binary matrix grid, return the length of the shortest clear path
from (0,0) to (n-1,n-1). If no such path exists, return -1.

A clear path:
- Visits only cells with value 0
- Moves in 8 directions (horizontal, vertical, diagonal)
- Length is number of visited cells in the path

Example 1:
  Input: grid = [
    [0,1,0],
    [1,0,0],
    [1,1,0]
  ]
  Output: 3

Example 2:
  Input: grid = [
    [1,0],
    [1,1]
  ]
  Output: -1

Constraints:
  1 <= n <= 100
  grid[i][j] is 0 or 1
'''


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        Return shortest clear path length in an n x n binary matrix.

        :param grid: n x n matrix of 0/1
        :return: shortest path length, or -1 if impossible
        """
        pass


# ========== TESTS ==========

def test_example1():
    """Example 1 -> 3."""
    sol = Solution()
    grid = [
        [0, 1, 0],
        [1, 0, 0],
        [1, 1, 0],
    ]
    assert_equal(sol.shortestPathBinaryMatrix(grid), 3)


def test_example2():
    """Example 2 -> -1 (start blocked)."""
    sol = Solution()
    grid = [
        [1, 0],
        [1, 1],
    ]
    assert_equal(sol.shortestPathBinaryMatrix(grid), -1)


if __name__ == "__main__":
    run_tests()