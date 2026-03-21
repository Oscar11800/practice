from neetcode75.test_runner import assert_equal, run_tests
from typing import Optional

"""
Subtree of Another Tree
Easy

Given the roots of two binary trees root and subRoot, return true if there is
a subtree of root with the same structure and node values of subRoot and false
otherwise.

A subtree of a binary tree is a tree that consists of a node in tree and all
of this node's descendants. The tree itself can also be considered a subtree
of itself.

Example 1:
Input: root = [1,2,3,4,5], subRoot = [2,4,5]
Output: true

Example 2:
Input: root = [1,2,3,4,5,null,null,6], subRoot = [2,4,5]
Output: false

Constraints:
1 <= The number of nodes in both trees <= 100
-100 <= root.val, subRoot.val <= 100
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        raise NotImplementedError


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
    assert_equal(sol.isSubtree(build_tree([1,2,3,4,5]), build_tree([2,4,5])), True)


def test_example2():
    sol = Solution()
    assert_equal(sol.isSubtree(build_tree([1,2,3,4,5,None,None,6]), build_tree([2,4,5])), False)


# Run: python3 -m neetcode75.trees.subtree_of_another_tree
if __name__ == "__main__":
    run_tests()
