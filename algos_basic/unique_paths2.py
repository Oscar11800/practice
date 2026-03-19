from typing import List
from test_runner import assert_equal, run_tests

'''
63. Unique Paths II

You are given an m x n grid obstacleGrid.
- 0 = open cell
- 1 = obstacle

A robot starts at top-left (0,0) and wants to reach bottom-right (m-1,n-1).
It can only move right or down.
Paths cannot go through obstacles.

Return number of unique valid paths.

Example 1:
  Input: obstacleGrid = [[0,0,0],[0,0,0],[0,1,0]]
  Output: 3

Example 2:
  Input: obstacleGrid = [[0,0,0],[0,0,1],[0,1,0]]
  Output: 0

Constraints:
  1 <= m, n <= 100
  obstacleGrid[i][j] is 0 or 1
'''


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        Return number of unique paths avoiding obstacles.

        :param obstacleGrid: 2D grid with 0 (space) and 1 (obstacle).
        :return: Number of unique valid paths.
        """
        pass


# ========== TESTS ==========

def test_example1():
    """Example 1 -> 3."""
    sol = Solution()
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 1, 0],
    ]
    assert_equal(sol.uniquePathsWithObstacles(grid), 3)


def test_example2():
    """Example 2 -> 0."""
    sol = Solution()
    grid = [
        [0, 0, 0],
        [0, 0, 1],
        [0, 1, 0],
    ]
    assert_equal(sol.uniquePathsWithObstacles(grid), 0)


if __name__ == "__main__":
    run_tests()