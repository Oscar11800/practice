from typing import List
from test_runner import assert_equal, run_tests
from collections import deque
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
        max_size = 0
        row_len, col_len = len(grid), len(grid[0])
        
        directions = [(1,0), (0, 1), (-1, 0), (0, -1)]

        def bfs(grid, row, col):
            queue = deque()
            grid[row][col] = 0
            queue.append((row, col))
            area = 1
            
            while queue:
                row, col = queue.popleft()
                for d in directions:
                    new_row = row + d[0]
                    new_col = col + d[1]
                    if not (0 <= new_row < row_len) or not (0 <= new_col < col_len) or grid[new_row][new_col] != 1:
                        continue
                    else:
                        area += 1
                        grid[new_row][new_col] = 0
                        queue.append((new_row, new_col))
            return area
            
        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j] == 1:
                    area = bfs(grid, i, j)
                    max_size = max(area, max_size)
        return max_size


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