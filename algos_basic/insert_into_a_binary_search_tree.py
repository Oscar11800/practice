from typing import Optional
from test_runner import assert_equal, run_tests

'''
701. Insert into a Binary Search Tree

You are given the root node of a binary search tree (BST) and a value val to insert into
the tree. Return the root node of the BST after the insertion. It is guaranteed that the
new value does not exist in the original BST.

Note: There may exist multiple valid ways for the insertion, as long as the tree remains
a BST after insertion. You can return any of them.

Example 1:
  Input: root = [5,3,9,1,4], val = 6
  Output: [5,3,9,1,4,6]

Example 2:
  Input: root = [5,3,6,null,4,null,10,null,null,7], val = 9
  Output: [5,3,6,null,4,null,10,null,null,7,null,null,9]

Constraints:
  0 <= number of nodes <= 10,000
  -10^8 <= val, Node.val <= 10^8
  All values are unique.
  val does not exist in the original BST.
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        Insert val into the BST and return the root.

        :param root: Root of the BST (may be None).
        :param val: Value to insert.
        :return: Root of the BST after insertion.
        """
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root


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


def tree_contains(root: Optional[TreeNode], val: int) -> bool:
    """Check if val exists in the BST."""
    while root:
        if root.val == val:
            return True
        root = root.left if val < root.val else root.right
    return False


# ========== TESTS ==========

def test_example1():
    """Example 1: insert 6 into [5,3,9,1,4]."""
    sol = Solution()
    root = build_tree([5, 3, 9, 1, 4])
    result = sol.insertIntoBST(root, 6)
    assert_equal(tree_contains(result, 6), True)
    assert_equal(sorted(tree_to_list(result)), [1, 3, 4, 5, 6, 9])


def test_example2():
    """Example 2: insert 9 into tree with nulls."""
    sol = Solution()
    root = build_tree([5, 3, 6, None, 4, None, 10, None, None, 7])
    result = sol.insertIntoBST(root, 9)
    assert_equal(tree_contains(result, 9), True)
    assert_equal(sorted(tree_to_list(result)), [3, 4, 5, 6, 7, 9, 10])


def test_empty_tree():
    """Empty tree: insert into None returns new node."""
    sol = Solution()
    result = sol.insertIntoBST(None, 5)
    assert result is not None
    assert_equal(result.val, 5)
    assert_equal(result.left, None)
    assert_equal(result.right, None)


if __name__ == "__main__":
    run_tests()
