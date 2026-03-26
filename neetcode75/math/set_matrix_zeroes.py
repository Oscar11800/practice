from typing import List
from neetcode75.test_runner import assert_equal, run_tests

"""
Set Matrix Zeroes
Medium

Given an m x n matrix of integers matrix, if an element is 0, set its entire row and column to 0's.

You must update the matrix in-place.

Follow up: Could you solve it using O(1) space?

Example 1:
Input: matrix = [[0,1],[1,0]]
Output: [[0,0],[0,0]]

Example 2:
Input: matrix = [[1,2,3],[4,0,5],[6,7,8]]
Output: [[1,0,3],[0,0,0],[6,0,8]]

Constraints:
1 <= matrix.length, matrix[0].length <= 100
-2^31 <= matrix[i][j] <= (2^31) - 1
"""


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        raise NotImplementedError


def test_example1():
    sol = Solution()
    matrix = [[0, 1], [1, 0]]
    sol.setZeroes(matrix)
    assert_equal(matrix, [[0, 0], [0, 0]])


def test_example2():
    sol = Solution()
    matrix = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
    sol.setZeroes(matrix)
    assert_equal(matrix, [[1, 0, 3], [0, 0, 0], [6, 0, 8]])


# Run: python3 -m neetcode75.math.set_matrix_zeroes
if __name__ == "__main__":
    run_tests()
