
from test_runner import assert_equal, run_tests
# TODO: complete this
'''
62. Unique Paths

There is an m x n grid. You can only move:
- right
- downm

Return the number of unique paths from top-left (0,0) to bottom-right (m-1,n-1).

You may assume answer fits in 32-bit integer.

Example 1:
  Input: m = 3, n = 6
  Output: 21

Example 2:
  Input: m = 3, n = 3
  Output: 6

Constraints:
  1 <= m, n <= 100
'''


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Return number of unique paths in m x n grid.

        :param m: Number of rows.
        :param n: Number of columns.
        :return: Count of unique paths.
        """
        memo = {}
        def dfs(row, col):
            if row >= m or col >= n or row < 0 or col < 0:
                return 0
            if (row, col) in memo:
                return memo[(row, col)]
            if row == 0 and col == 0:
                memo[(row, col)] = 1
                return
            
            if memo[row-1, col] != -1:
                down = memo[(row-1, col)]
            else:
                dfs(row-1, col)
                down = memo[(row-1, col)]
            if memo[row, col-1] != -1:
                left = memo[(row, col-1)]
            else:
                dfs(row, col -1)
                left = memo[(row, col-1)]
            
            memo[(row, col)] = left + down
        dfs(m-1, n-1)
        return memo[(m-1,n-1)]

# ========== TESTS ==========

def test_example1():
    """Example 1: 3x6 -> 21."""
    sol = Solution()
    assert_equal(sol.uniquePaths(3, 6), 21)


def test_example2():
    """Example 2: 3x3 -> 6."""
    sol = Solution()
    assert_equal(sol.uniquePaths(3, 3), 6)


if __name__ == "__main__":
    run_tests()