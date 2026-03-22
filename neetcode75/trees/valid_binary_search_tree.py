from neetcode75.test_runner import assert_equal, run_tests
from typing import Optional

"""
Valid Binary Search Tree
Medium

Given the root of a binary tree, return true if it is a valid binary search
tree, otherwise return false.

A valid binary search tree satisfies the following constraints:
- The left subtree of every node contains only nodes with keys less than the
  node's key.
- The right subtree of every node contains only nodes with keys greater than
  the node's key.
- Both the left and right subtrees are also binary search trees.

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [1,2,3]
Output: false
Explanation: The root node's value is 1 but its left child's value is 2 which
is greater than 1.

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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = None
        def dfs(node):
            if not node:
                return True
            if not dfs(node.left):
                return False
            if self.prev is not None and node.val <= self.prev.val:
                return False 
            self.prev = node
            return dfs(node.right)
        return dfs(root)

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
    assert_equal(sol.isValidBST(build_tree([2,1,3])), True)

 
def test_example2():
    sol = Solution()
    assert_equal(sol.isValidBST(build_tree([1,2,3])), False)


# Run: python3 -m neetcode75.trees.valid_binary_search_tree
if __name__ == "__main__":
    run_tests()
