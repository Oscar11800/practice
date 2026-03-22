from neetcode75.test_runner import assert_equal, run_tests
from typing import List

"""
Graph Valid Tree
Medium

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each
edge is a pair of nodes), write a function to check whether these edges make
up a valid tree.

Note: You can assume that no duplicate edges will appear in edges. Since all
edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear
together in edges.

Example 1:
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true

Example 2:
Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false

Constraints:
1 <= n <= 100
0 <= edges.length <= n * (n - 1) / 2
"""


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        # construct adj list
        adj = [[] for _ in range(n)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        # dfs
        self.visited = set()
        def dfs(node):
            self.visited.add(node)
            for neighbor in adj[node]:
                if neighbor not in self.visited:
                    dfs(neighbor)
        dfs(0)
        return len(self.visited) == n


def test_example1():
    sol = Solution()
    assert_equal(sol.validTree(5, [[0,1],[0,2],[0,3],[1,4]]), True)


def test_example2():
    sol = Solution()
    assert_equal(sol.validTree(5, [[0,1],[1,2],[2,3],[1,3],[1,4]]), False)


# Run: python3 -m neetcode75.backtracking_and_graphs.graph_valid_tree
if __name__ == "__main__":
    run_tests()
