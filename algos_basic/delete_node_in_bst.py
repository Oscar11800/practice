from typing import Optional
from test_runner import assert_equal, run_tests

'''
450. Delete Node in a BST

You are given a root node reference of a BST and a key. Delete the node with the given
key in the BST, if present. Return the root node reference (possibly updated) of the BST.

The deletion can be divided into two stages:
1. Search for a node to remove.
2. If the node is found, delete the node.

Note: There can be multiple valid results after deleting the node, return any one of them.

Example 1:
  Input: root = [5,3,9,1,4], key = 3
  Output: [5,4,9,1]
  Explanation: Another valid answer is [5,1,9,null,4]

Example 2:
  Input: root = [5,3,6,null,4,null,10,null,null,7], key = 3
  Output: [5,4,6,null,null,null,10,7]

Constraints:
  0 <= number of nodes <= 10,000
  -10^5 <= key, Node.val <= 10^5
  All values are unique.
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        Delete the node with value key from the BST and return the root.

        :param root: Root of the BST.
        :param key: Value of the node to delete.
        :return: Root of the BST after deletion (possibly updated).
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


def tree_to_list(root: Optional[TreeNode]) -> list:
    """Convert tree to level-order list."""
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


def tree_contains(root: Optional[TreeNode], val: int) -> bool:
    """Check if val exists in the BST."""
    while root:
        if root.val == val:
            return True
        root = root.left if val < root.val else root.right
    return False


# ========== TESTS ==========

def test_example1():
    """Example 1: delete 3 from [5,3,9,1,4]."""
    sol = Solution()
    root = build_tree([5, 3, 9, 1, 4])
    result = sol.deleteNode(root, 3)
    assert_equal(tree_contains(result, 3), False)
    assert_equal(sorted(tree_to_list(result)), [1, 4, 5, 9])


def test_example2():
    """Example 2: delete 3 from tree with nulls."""
    sol = Solution()
    root = build_tree([5, 3, 6, None, 4, None, 10, None, None, 7])
    result = sol.deleteNode(root, 3)
    assert_equal(tree_contains(result, 3), False)
    assert_equal(sorted(tree_to_list(result)), [4, 5, 6, 7, 10])


def test_key_not_found():
    """Key not in tree: return tree unchanged."""
    sol = Solution()
    root = build_tree([5, 3, 9, 1, 4])
    result = sol.deleteNode(root, 99)
    assert_equal(sorted(tree_to_list(result)), [1, 3, 4, 5, 9])


if __name__ == "__main__":
    run_tests()
