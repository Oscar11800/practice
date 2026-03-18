from collections import deque
from typing import List
from test_runner import assert_equal, run_tests

'''
994. Rotting Fruit (Rotting Oranges)

Given a 2D matrix grid:
- 0 = empty cell
- 1 = fresh fruit
- 2 = rotten fruit

Every minute, fresh fruit adjacent (up/down/left/right) to rotten fruit becomes rotten.

Return the minimum minutes until no fresh fruit remains.
If impossible, return -1.

Example 1:
  Input: grid = [[1,1,0],[0,1,1],[0,1,2]]
  Output: 4

Example 2:
  Input: grid = [[1,0,1],[0,2,0],[1,0,1]]
  Output: -1

Constraints:
  1 <= rows, cols <= 10
'''


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Return minimum minutes to rot all fresh fruit, or -1 if impossible.

        :param grid: 2D matrix of 0/1/2.
        :return: Minutes needed, or -1.
        """
        queue = deque()
        fresh_count = 0
        minutes = 0
        row_len, col_len = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        # initial fresh fruit count, setting rotten to queue
        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j] == 1:
                    fresh_count += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))
        # edge case no fresh fruit
        if fresh_count == 0:
            return 0
        
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for d in directions:
                    new_row, new_col = row + d[0], col + d[1]
                    if not 0 <= new_row < row_len or not 0 <= new_col < col_len or not grid[new_row][new_col] == 1:
                        continue
                    queue.append((new_row, new_col))
                    grid[new_row][new_col] = 2
                    fresh_count -= 1
            minutes += 1
            if fresh_count == 0:
                return minutes

        return -1


# ========== TESTS ==========

def test_example1():
    """Example 1 -> 4."""
    sol = Solution()
    grid = [
        [1, 1, 0],
        [0, 1, 1],
        [0, 1, 2],
    ]
    assert_equal(sol.orangesRotting(grid), 4)


def test_example2():
    """Example 2 -> -1 (isolated fresh fruit)."""
    sol = Solution()
    grid = [
        [1, 0, 1],
        [0, 2, 0],
        [1, 0, 1],
    ]
    assert_equal(sol.orangesRotting(grid), -1)


if __name__ == "__main__":
    run_tests()