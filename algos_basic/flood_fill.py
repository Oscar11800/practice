from typing import List
from test_runner import assert_equal, run_tests

'''
733. Flood Fill

You are given an image represented by an m x n integer grid image, where image[i][j]
represents the pixel value of the image.

You are also given three integers:
- sr: starting row
- sc: starting column
- color: new color value

Perform a flood fill from pixel (sr, sc):
- Replace the starting pixel's original color
- Replace all 4-directionally connected pixels (up/down/left/right) with the same
  original color
- Return the modified image

Example 1:
  Input:
    image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
  Output:
    [[2,2,2],[2,2,0],[2,0,1]]

Example 2:
  Input:
    image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
  Output:
    [[0,0,0],[0,0,0]]

Constraints:
  1 <= m, n <= 50
  0 <= image[i][j], color < 2^16
  0 <= sr < m
  0 <= sc < n
'''


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """
        Return the image after flood filling from (sr, sc).

        :param image: 2D grid of pixel values.
        :param sr: Start row.
        :param sc: Start col.
        :param color: Replacement color.
        :return: Modified image.
        """
        pass


# ========== TESTS ==========

def test_example1():
    """Example 1."""
    sol = Solution()
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    expected = [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
    assert_equal(sol.floodFill(image, 1, 1, 2), expected)


def test_example2():
    """Example 2: new color equals original color."""
    sol = Solution()
    image = [[0, 0, 0], [0, 0, 0]]
    expected = [[0, 0, 0], [0, 0, 0]]
    assert_equal(sol.floodFill(image, 0, 0, 0), expected)


if __name__ == "__main__":
    run_tests()