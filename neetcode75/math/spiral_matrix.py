from typing import List
from neetcode75.test_runner import assert_equal, run_tests

"""
Spiral Matrix
Medium

Given an m x n matrix of integers matrix, return a list of all elements within the matrix in spiral order.

Example 1:
Input: matrix = [[1,2],[3,4]]
Output: [1,2,4,3]

Example 2:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 3:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
1 <= matrix.length, matrix[i].length <= 10
-100 <= matrix[i][j] <= 100
"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        raise NotImplementedError


def test_example1():
    sol = Solution()
    assert_equal(sol.spiralOrder([[1, 2], [3, 4]]), [1, 2, 4, 3])


def test_example2():
    sol = Solution()
    assert_equal(
        sol.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
        [1, 2, 3, 6, 9, 8, 7, 4, 5],
    )


def test_example3():
    sol = Solution()
    assert_equal(
        sol.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]),
        [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
    )


# Run: python3 -m neetcode75.math.spiral_matrix
if __name__ == "__main__":
    run_tests()
