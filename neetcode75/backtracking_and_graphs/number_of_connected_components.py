from neetcode75.test_runner import assert_equal, run_tests
from typing import List

"""
Number of Connected Components in an Undirected Graph
Medium

You have a graph of n nodes. You are given an integer n and an array edges
where edges[i] = [ai, bi] indicates that there is an edge between ai and bi
in the graph.

Return the number of connected components in the graph.

Example 1:
Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2

Example 2:
Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1

Constraints:
1 <= n <= 2000
1 <= edges.length <= 5000
edges[i].length == 2
0 <= ai <= bi < n
ai != bi
There are no repeated edges
"""


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        raise NotImplementedError


def test_example1():
    sol = Solution()
    assert_equal(sol.countComponents(5, [[0,1],[1,2],[3,4]]), 2)


def test_example2():
    sol = Solution()
    assert_equal(sol.countComponents(5, [[0,1],[1,2],[2,3],[3,4]]), 1)


# Run: python3 -m neetcode75.backtracking_and_graphs.number_of_connected_components
if __name__ == "__main__":
    run_tests()
