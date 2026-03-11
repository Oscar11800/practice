from test_runner import assert_equal, run_tests

'''
74. Search a 2D Matrix

You are given an m x n 2-D integer array matrix and an integer target.

- Each row in matrix is sorted in non-decreasing order.
- The first integer of every row is greater than the last integer of the previous row.

Return true if target exists within matrix, or false otherwise.

Can you write a solution that runs in O(log(m * n)) time?

Example 1:
  Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10
  Output: true

Example 2:
  Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15
  Output: false
'''


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """
        Search for target in the 2D matrix.

        :param matrix: m x n matrix, rows sorted, each row's first > previous row's last.
        :param target: Value to search for.
        :return: True if target exists, False otherwise.
        """
        n = len(matrix)
        m = len(matrix[0])
        l, r = 0, n*m-1
        mid = (l + r)//2

        row = mid // m
        col = mid % m

        while l <= r:
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                r = mid - 1
                mid = (l + r)//2
                row = mid // m
                col = mid % m
            else:
                l = mid + 1
                mid = (l + r)//2
                row = mid // m
                col = mid % m

        return False


# ========== TESTS ==========

def test_example1():
    """Example 1: target 10 exists."""
    sol = Solution()
    matrix = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]]
    assert_equal(sol.searchMatrix(matrix, 10), True)


def test_example2():
    """Example 2: target 15 does not exist."""
    sol = Solution()
    matrix = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]]
    assert_equal(sol.searchMatrix(matrix, 15), False)


if __name__ == "__main__":
    run_tests()
