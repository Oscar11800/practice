from neetcode75.test_runner import assert_equal, run_tests
from typing import Optional
from collections import deque

"""
Maximum Depth of Binary Tree
Easy

Given the root of a binary tree, return its depth.

The depth of a binary tree is defined as the number of nodes along the longest
path from the root node down to the farthest leaf node.

Example 1:
Input: root = [1,2,3,null,null,4]
Output: 3

Example 2:
Input: root = []
Output: 0

Constraints:
0 <= The number of nodes in the tree <= 100
-100 <= Node.val <= 100
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque()
        queue.append(root)
        max_depth = 0

        while queue:
            max_depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return max_depth




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
    assert_equal(sol.maxDepth(build_tree([1,2,3,None,None,4])), 3)


def test_example2():
    sol = Solution()
    assert_equal(sol.maxDepth(None), 0)


# Run: python3 -m neetcode75.trees.maximum_depth_of_binary_tree
if __name__ == "__main__":
    run_tests()
