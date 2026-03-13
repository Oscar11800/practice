from typing import Optional, List
from test_runner import assert_equal, run_tests

'''
102. Binary Tree Level Order Traversal

Given a binary tree root, return the level order traversal of it as a nested list,
where each sublist contains the values of nodes at a particular level in the tree,
from left to right.

Example 1:
  Input: root = [1,2,3,4,5,6,7]
  Output: [[1],[2,3],[4,5,6,7]]

Example 2:
  Input: root = [1]
  Output: [[1]]

Example 3:
  Input: root = []
  Output: []
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Return level order traversal as nested lists.

        :param root: Root of the binary tree.
        :return: List of lists, each sublist contains node values at that level.
        """
        pass


# ========== HELPERS ==========

def build_tree(arr: list) -> Optional[TreeNode]:
    """Build tree from level-order list (None for missing nodes)."""
    if not arr or arr[0] is None:
        return None
    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    while queue and i < len(arr):
        node = queue.pop(0)
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
    return root


# ========== TESTS ==========

def test_example1():
    """Example 1: [1,2,3,4,5,6,7] -> [[1],[2,3],[4,5,6,7]]."""
    sol = Solution()
    root = build_tree([1, 2, 3, 4, 5, 6, 7])
    assert_equal(sol.levelOrder(root), [[1], [2, 3], [4, 5, 6, 7]])


def test_example2():
    """Example 2: [1] -> [[1]]."""
    sol = Solution()
    root = build_tree([1])
    assert_equal(sol.levelOrder(root), [[1]])


def test_example3():
    """Example 3: [] -> []."""
    sol = Solution()
    root = build_tree([])
    assert_equal(sol.levelOrder(root), [])


if __name__ == "__main__":
    run_tests()
