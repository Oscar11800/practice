from neetcode75.test_runner import assert_equal, run_tests
from typing import Optional

"""
Binary Tree Maximum Path Sum

Given the root of a non-empty binary tree, return the maximum path sum of any
non-empty path.

A path in a binary tree is a sequence of nodes where each pair of adjacent
nodes has an edge connecting them. A node can not appear in the sequence more
than once. The path does not necessarily need to include the root.

The path sum of a path is the sum of the node's values in the path.

Example 1:
Input: root = [1,2,3]
Output: 6
Explanation: The path is 2 -> 1 -> 3 with a sum of 2 + 1 + 3 = 6.

Example 2:
Input: root = [-15,10,20,null,null,15,5,-5]
Output: 40
Explanation: The path is 15 -> 20 -> 5 with a sum of 15 + 20 + 5 = 40.

Constraints:
1 <= The number of nodes in the tree <= 1000
-1000 <= Node.val <= 1000
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = root.val
        def dfs(node):
            if node is None:
                return 0
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))
            self.max_sum = max(self.max_sum, node.val + left + right)
            return max(node.val, node.val + left, node.val + right)
        dfs(root)
        return self.max_sum



def build_tree(vals):
    if not vals:
        return None
    nodes = [TreeNode(v) if v is not None else None for v in vals]
    for i, node in enumerate(nodes):
        if node:
            left_i, right_i = 2 * i + 1, 2 * i + 2
            if left_i < len(nodes):
                node.left = nodes[left_i]
            if right_i < len(nodes):
                node.right = nodes[right_i]
    return nodes[0]


def test_example1():
    sol = Solution()
    assert_equal(sol.maxPathSum(build_tree([1,2,3])), 6)


def test_example2():
    sol = Solution()
    assert_equal(sol.maxPathSum(build_tree([-15,10,20,None,None,15,5,-5])), 40)


# Run: python3 -m neetcode75.trees.binary_tree_maximum_path_sum
if __name__ == "__main__":
    run_tests()
