from typing import List
from test_runner import assert_equal, run_tests

'''
200. Number of Islands

Given a 2D grid where '1' is land and '0' is water, return the number of islands.

An island is formed by horizontally/vertically adjacent lands and is surrounded by water.
You may assume all edges are water.

Example 1:
  Input: grid = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]
  Output: 1

Example 2:
  Input: grid = [
    ["1","1","0","0","1"],
    ["1","1","0","0","1"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
  ]
  Output: 4

Constraints:
  1 <= rows, cols <= 100
  grid[i][j] is '0' or '1'
'''


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Return the number of islands in grid.

        :param grid: 2D grid of '0' and '1'
        :return: Number of islands
        """
        counter = 2
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        row_len, col_len = len(grid), len(grid[0])

        def dfs(grid, row, col, counter):
            if 0 <= row < row_len and 0 <= col < col_len and grid[row][col] == "1":
                grid[row][col] = counter
            else:
                return
            for d in directions:
                dfs(grid, row + d[0], col + d[1], counter)
        
        
        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j] == "1":
                    dfs(grid, i, j, counter)
                    counter += 1
        return counter - 2


# ========== TESTS ==========

def test_example1():
    """Example 1 -> 1."""
    sol = Solution()
    grid = [
        ["0", "1", "1", "1", "0"],
        ["0", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    assert_equal(sol.numIslands(grid), 1)


def test_example2():
    """Example 2 -> 4."""
    sol = Solution()
    grid = [
        ["1", "1", "0", "0", "1"],
        ["1", "1", "0", "0", "1"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    assert_equal(sol.numIslands(grid), 4)


if __name__ == "__main__":
    run_tests()