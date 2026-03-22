from neetcode75.test_runner import assert_equal, run_tests
from typing import List

"""
Number of Connected Components in an Undirected Graph
Medium

You have a graph of n nodes. You are given an integer n and an array edges
where edges[i] = [ai, bi] indicates that there is an edge between ai and bi
in the graph.
self.Return the number of connected components in the graph.

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
        parents = [i for i in range(n)]
        ranks = [0 for _ in range(n)]

        def find(node):
            while parents[node] != node:
                parents[node] = parents[parents[node]]
                node = parents[node]
            return parents[node]
        def union(n1, n2):
            node1, node2 = find(n1), find(n2)
            if node1 == node2:
                return False
            rank1, rank2 = ranks[node1], ranks[node2]
            if rank1 <= rank2:
                parents[node1] = node2
            elif rank1 > rank2:
                ranks[node2] += 1
            else:
                parents[node1] = node2
                ranks[node1] += 1
            return True
        unions = 0
        for edge in edges:
            a, b = edge
            if union(a, b):
                unions += 1
        return n - unions

def test_example1():
    sol = Solution()
    assert_equal(sol.countComponents(5, [[0,1],[1,2],[3,4]]), 2)


def test_example2():
    sol = Solution()
    assert_equal(sol.countComponents(5, [[0,1],[1,2],[2,3],[3,4]]), 1)


# Run: python3 -m neetcode75.backtracking_and_graphs.number_of_connected_components
if __name__ == "__main__":
    run_tests()
