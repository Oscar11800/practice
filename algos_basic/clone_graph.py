from typing import Optional, List
from test_runner import assert_equal, run_tests

'''
133. Clone Graph

Given a node in a connected undirected graph, return a deep copy of the graph.

Each node contains:
- val: int
- neighbors: List[Node]

Graph is represented in tests as adjacency list (1-indexed node values).

Example 1:
  Input: adjList = [[2],[1,3],[2]]
  Output: [[2],[1,3],[2]]

Example 2:
  Input: adjList = [[]]
  Output: [[]]

Example 3:
  Input: adjList = []
  Output: []

Constraints:
  0 <= number of nodes <= 100
  1 <= Node.val <= 100
  No duplicate edges, no self-loops.
'''


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        """
        Return a deep copy of the graph starting from node.

        :param node: Start node of connected graph (or None).
        :return: Deep-cloned start node.
        """
        pass


# ========== HELPERS ==========

def build_graph(adj_list: List[List[int]]) -> Optional[Node]:
    """Build graph from 1-indexed adjacency list."""
    if not adj_list:
        return None
    nodes = [Node(i + 1) for i in range(len(adj_list))]
    for i, neighbors in enumerate(adj_list):
        nodes[i].neighbors = [nodes[n - 1] for n in neighbors]
    return nodes[0]


def graph_to_adj_list(node: Optional[Node]) -> List[List[int]]:
    """Serialize connected component starting from node to adjacency list."""
    if node is None:
        return []

    seen = {}
    order = []
    queue = [node]
    seen[node] = 1

    while queue:
        cur = queue.pop(0)
        order.append(cur)
        for nei in cur.neighbors:
            if nei not in seen:
                seen[nei] = len(seen) + 1
                queue.append(nei)

    # Map by node val to match problem's 1-indexed val convention
    max_val = max(n.val for n in order)
    out = [[] for _ in range(max_val)]
    for n in order:
        out[n.val - 1] = sorted(nei.val for nei in n.neighbors)
    return out


# ========== TESTS ==========

def test_example1():
    """Example 1: [[2],[1,3],[2]]."""
    sol = Solution()
    root = build_graph([[2], [1, 3], [2]])
    clone = sol.cloneGraph(root)
    assert_equal(graph_to_adj_list(clone), [[2], [1, 3], [2]])


def test_example2():
    """Example 2: [[]]."""
    sol = Solution()
    root = build_graph([[]])
    clone = sol.cloneGraph(root)
    assert_equal(graph_to_adj_list(clone), [[]])


def test_example3():
    """Example 3: []."""
    sol = Solution()
    root = build_graph([])
    clone = sol.cloneGraph(root)
    assert_equal(graph_to_adj_list(clone), [])


if __name__ == "__main__":
    run_tests()