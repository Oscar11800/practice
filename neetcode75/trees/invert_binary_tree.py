from neetcode75.test_runner import assert_equal, run_tests
from typing import Optional
from collections import deque
"""
Invert Binary Tree
Easy

You are given the root of a binary tree. Invert the binary tree and return its root.

Example 1:
Input: root = [1,2,3,4,5,6,7]
Output: [1,3,2,7,6,5,4]

Example 2:
Input: root = [3,2,1]
Output: [3,1,2]

Example 3:
Input: root = []
Output: []

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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
       if not root:
           return root
       q = deque()
       q.append(root)

       while q:
           node = q.popleft()
           temp = node.left
           node.left = node.right
           node.right = temp
           if node.right:
               q.append(node.right)
           if node.left:
               q.append(node.left)
       return root


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


def tree_to_list(root):
    if not root:
        return []
    result, queue = [], [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result


def test_example1():
    sol = Solution()
    assert_equal(tree_to_list(sol.invertTree(build_tree([1,2,3,4,5,6,7]))), [1,3,2,7,6,5,4])


def test_example2():
    sol = Solution()
    assert_equal(tree_to_list(sol.invertTree(build_tree([3,2,1]))), [3,1,2])


def test_example3():
    sol = Solution()
    assert_equal(tree_to_list(sol.invertTree(None)), [])


# Run: python3 -m neetcode75.trees.invert_binary_tree
if __name__ == "__main__":
    run_tests()
