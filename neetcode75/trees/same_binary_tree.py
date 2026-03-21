from neetcode75.test_runner import assert_equal, run_tests
from typing import Optional

"""
Same Binary Tree
Easy

Given the roots of two binary trees p and q, return true if the trees are
equivalent, otherwise return false.

Two binary trees are considered equivalent if they share the exact same
structure and the nodes have the same values.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [4,7], q = [4,null,7]
Output: false

Example 3:
Input: p = [1,2,3], q = [1,3,2]
Output: false

Constraints:
0 <= The number of nodes in both trees <= 100
-100 <= Node.val <= 100
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and not q:
            return False
        if q and not p:
            return False

        stack = [(p, q)]
        while stack:
            p_node, q_node = stack.pop()
            if p_node.val != q_node.val:
                return False
            if p_node.left:
                if not q_node.left:
                    return False
                stack.append((p_node.left, q_node.left))
            else:
                if q_node.left:
                    return False
            if p_node.right:
                if not q_node.right:
                    return False
                stack.append((p_node.right, q_node.right))
            else:
                if q_node.right:
                    return False
        return True


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
    assert_equal(sol.isSameTree(build_tree([1,2,3]), build_tree([1,2,3])), True)


def test_example2():
    sol = Solution()
    assert_equal(sol.isSameTree(build_tree([4,7]), build_tree([4,None,7])), False)


def test_example3():
    sol = Solution()
    assert_equal(sol.isSameTree(build_tree([1,2,3]), build_tree([1,3,2])), False)


# Run: python3 -m neetcode75.trees.same_binary_tree
if __name__ == "__main__":
    run_tests()
