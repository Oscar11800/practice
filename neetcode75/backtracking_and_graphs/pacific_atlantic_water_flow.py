from neetcode75.test_runner import assert_equal, run_tests
from typing import List
from collections import deque
"""
Pacific Atlantic Water Flow
Medium

You are given a rectangular island heights where heights[r][c] represents the
height above sea level of the cell at coordinate (r, c).

The island borders the Pacific Ocean from the top and left sides, and borders
the Atlantic Ocean from the bottom and right sides.

Water can flow in four directions (up, down, left, or right) from a cell to a
neighboring cell with height equal or lower. Water can also flow into the ocean
from cells adjacent to the ocean.

Find all cells where water can flow from that cell to both the Pacific and
Atlantic oceans. Return it as a 2D list where each element is a list [r, c]
representing the row and column of the cell. You may return the answer in any
order.

Example 1:
Input: heights = [
  [4,2,7,3,4],
  [7,4,6,4,7],
  [6,3,5,3,6]
]
Output: [[0,2],[0,4],[1,0],[1,1],[1,2],[1,3],[1,4],[2,0]]

Example 2:
Input: heights = [[1],[1]]
Output: [[0,0],[1,0]]

Constraints:
1 <= heights.length, heights[r].length <= 100
0 <= heights[r][c] <= 1000
"""


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        queue = deque()
        pac, atl = set(), set()
        n, m = len(heights), len(heights[0])
        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]

        # init pac
        for i in range(m):
            queue.append((0, i))
        for i in range(n):
            queue.append((i, 0))

        while queue:
            coord = queue.pop()
            pac.add(coord)
            for d in directions:
                new_row, new_col = coord[0] + d[0], coord[1] + d[1]
                new_coord = (new_row, new_col)
                if new_coord not in pac and 0 <= new_row < n and 0 <= new_col < m and heights[new_row][new_col] >= heights[coord[0]][coord[1]]:
                    queue.append(new_coord)

        # init atl
        for i in range(m):
            queue.append((n-1, i))
        for i in range(n):
            queue.append((i, m-1))

        while queue:
            coord = queue.pop()
            atl.add(coord)
            for d in directions:
                new_row, new_col = coord[0] + d[0], coord[1] + d[1]
                new_coord = (new_row, new_col)
                if new_coord not in atl and 0 <= new_row < n and 0 <= new_col < m and heights[new_row][new_col] >= heights[coord[0]][coord[1]]:
                    queue.append(new_coord)

        return [list(coord) for coord in pac & atl]




def test_example1():
    sol = Solution()
    heights = [
        [4,2,7,3,4],
        [7,4,6,4,7],
        [6,3,5,3,6]
    ]
    result = sol.pacificAtlantic(heights)
    assert_equal(sorted(result), sorted([[0,2],[0,4],[1,0],[1,1],[1,2],[1,3],[1,4],[2,0]]))


def test_example2():
    sol = Solution()
    assert_equal(sorted(sol.pacificAtlantic([[1],[1]])), sorted([[0,0],[1,0]]))


# Run: python3 -m neetcode75.backtracking_and_graphs.pacific_atlantic_water_flow
if __name__ == "__main__":
    run_tests()
