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
        pass


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