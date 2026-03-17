from typing import List
from test_runner import assert_equal, run_tests
import heapq

'''
973. K Closest Points to Origin

You are given a 2D array points where points[i] = [xi, yi] and an integer k.

Return the k closest points to the origin (0, 0).
Distance = Euclidean: sqrt((x1-x2)^2 + (y1-y2)^2).

You may return the answer in any order.

Example 1:
  Input: points = [[0,2],[2,2]], k = 1
  Output: [[0,2]]
  Explanation: (0,2) dist=2, (2,2) dist=2.828; closest is (0,2)

Example 2:
  Input: points = [[0,2],[2,0],[2,2]], k = 2
  Output: [[0,2],[2,0]]  (or [2,0],[0,2])

Constraints:
  1 <= k <= points.length <= 1000
  -100 <= points[i][0], points[i][1] <= 100
'''


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Return the k closest points to the origin.

        :param points: List of [x, y] coordinates.
        :param k: Number of closest points to return.
        :return: k closest points (any order).
        """
        rtn = []
        min_heap = list(map(lambda point: (point[0] ** 2 + point[1] ** 2, point), points))
        heapq.heapify(min_heap)
        for _ in range(k):
            rtn.append(heapq.heappop(min_heap)[1])
        return rtn


# ========== HELPERS ==========

def normalize_points(pts: List[List[int]]) -> List[List[int]]:
    """Sort for comparison (output order doesn't matter)."""
    return sorted(pts)


# ========== TESTS ==========

def test_example1():
    """Example 1: [[0,2],[2,2]], k=1 -> [[0,2]]."""
    sol = Solution()
    expected = [[0, 2]]
    assert_equal(normalize_points(sol.kClosest([[0, 2], [2, 2]], 1)), normalize_points(expected))


def test_example2():
    """Example 2: [[0,2],[2,0],[2,2]], k=2 -> [[0,2],[2,0]]."""
    sol = Solution()
    expected = [[0, 2], [2, 0]]
    assert_equal(normalize_points(sol.kClosest([[0, 2], [2, 0], [2, 2]], 2)), normalize_points(expected))


if __name__ == "__main__":
    run_tests()