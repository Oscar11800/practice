from typing import List
from test_runner import assert_equal, run_tests

'''
695. Max Area of Island

You are given a matrix grid where each cell is:
- 0 = water
- 1 = land

An island is a group of 1s connected horizontally or vertically.
All grid edges are surrounded by water.

Area of an island = number of cells in that island.

Return the maximum island area. If no island exists, return 0.

Example 1:
  Input: grid = [
    [0,1,1,0,1],
    [1,0,1,0,1],
    [0,1,1,0,1],
    [0,1,0,0,1]
  ]
  Output: 6

Constraints:
  1 <= rows, cols <= 50
'''


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Return maximum island area in the grid.

        :param grid: 2D matrix of 0/1.
        :return: Maximum island area, or 0 if none.
        """
        pass


# ========== TESTS ==========

def test_example1():
    """Example 1 -> 6."""
    sol = Solution()
    grid = [
        [0, 1, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [0, 1, 1, 0, 1],
        [0, 1, 0, 0, 1],
    ]
    assert_equal(sol.maxAreaOfIsland(grid), 6)


def test_no_island():
    """All water -> 0."""
    sol = Solution()
    grid = [
        [0, 0],
        [0, 0],
    ]
    assert_equal(sol.maxAreaOfIsland(grid), 0)


if __name__ == "__main__":
    run_tests()