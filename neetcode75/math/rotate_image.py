from typing import List
from neetcode75.test_runner import assert_equal, run_tests

"""
Rotate Image

Given a square n x n matrix of integers matrix, rotate it by 90 degrees clockwise.

You must rotate the matrix in-place. Do not allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix = [[1,2],[3,4]]
Output: [[3,1],[4,2]]

Example 2:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Constraints:
n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
"""


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in len(n):
            for _ in range(4):
                top 

                             

                              



def test_example1():
    sol = Solution()
    matrix = [[1, 2], [3, 4]]
    sol.rotate(matrix)
    assert_equal(matrix, [[3, 1], [4, 2]])


def test_example2():
    sol = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    sol.rotate(matrix)
    assert_equal(matrix, [[7, 4, 1], [8, 5, 2], [9, 6, 3]])


# Run: python3 -m neetcode75.math.rotate_image
if __name__ == "__main__":
    run_tests()
