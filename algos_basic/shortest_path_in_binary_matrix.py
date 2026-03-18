from typing import List
from test_runner import assert_equal, run_tests
from collections import deque
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
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        row_len, col_len = len(grid), len(grid[0])
        queue = deque()
        visited = set()
        queue.append((0,0))
        visited.add((0, 0))
        length = 1
        directions = [(1,0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                if row == row_len - 1 and col == col_len - 1:
                    return length
                for direction in directions:
                    new_row, new_col = row + direction[0], col + direction[1]
                    if not 0 <= new_row < row_len or not 0 <= new_col < col_len or grid[new_row][new_col] != 0 or (new_row, new_col) in visited:
                        continue
                    visited.add((new_row, new_col))
                    queue.append((new_row, new_col))
            length += 1

        
        return -1


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