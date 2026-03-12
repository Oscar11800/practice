from typing import Optional
from test_runner import assert_equal, run_tests

'''
700. Search in a Binary Search Tree

You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted
with that node. If such a node does not exist, return null.

Example 1:
  Input: root = [4,2,7,1,3], val = 2
  Output: [2,1,3]

Example 2:
  Input: root = [4,2,7,1,3], val = 5
  Output: []

Constraints:
  Number of nodes in [1, 5000]
  1 <= Node.val <= 10^7
  1 <= val <= 10^7
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        Find the node with value val in the BST and return its subtree.

        :param root: Root of the BST.
        :param val: Value to search for.
        :return: Subtree rooted at the node, or None if not found.
        """
        while root:
            if root.val == val:
                return root
            root = root.left if val < root.val else root.right
        return None


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


def tree_to_list(root: Optional[TreeNode]) -> list:
    """Convert tree to level-order list for comparison."""
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


# ========== TESTS ==========

def test_example1():
    """Example 1: find 2 -> subtree [2,1,3]."""
    sol = Solution()
    root = build_tree([4, 2, 7, 1, 3])
    result = sol.searchBST(root, 2)
    assert_equal(tree_to_list(result), [2, 1, 3])


def test_example2():
    """Example 2: find 5 -> not found, return []."""
    sol = Solution()
    root = build_tree([4, 2, 7, 1, 3])
    result = sol.searchBST(root, 5)
    assert_equal(tree_to_list(result), [])


if __name__ == "__main__":
    run_tests()
