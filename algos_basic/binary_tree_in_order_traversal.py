from typing import Optional
from test_runner import assert_equal, run_tests

'''
94. Binary Tree Inorder Traversal

You are given the root of a binary tree. Return the inorder traversal of its nodes' values.

Inorder: left → root → right

Example 1:
  Input: root = [1,2,3,4,5,6,7]
  Output: [4,2,5,1,6,3,7]

Example 2:
  Input: root = [1,2,3,null,4,5,null]
  Output: [2,4,1,5,3]

Example 3:
  Input: root = []
  Output: []

Constraints:
  0 <= number of nodes <= 100
  -100 <= Node.val <= 100

Follow up: Recursive solution is trivial, could you do it iteratively?
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversalRecursive(self, root: Optional[TreeNode]) -> list[int]:
        """
        Inorder traversal using recursion.
        """
        if root:
            left = self.inorderTraversalRecursive(root.left)
            right = self.inorderTraversalRecursive(root.right)
            return left + [root.val] + right
        return []

    def inorderTraversalIterative(self, root: Optional[TreeNode]) -> list[int]:
        """
        Inorder traversal using iteration (stack, no recursion).
        """
        curr = root
        stack = []
        res = []

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right

        return res


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
    """Example 1: [1,2,3,4,5,6,7] -> [4,2,5,1,6,3,7]."""
    sol = Solution()
    root = build_tree([1, 2, 3, 4, 5, 6, 7])
    result_rec = sol.inorderTraversalRecursive(root)
    result_iter = sol.inorderTraversalIterative(root)
    assert_equal(result_rec, [4, 2, 5, 1, 6, 3, 7])
    assert_equal(result_iter, [4, 2, 5, 1, 6, 3, 7])


def test_example2():
    """Example 2: [1,2,3,null,4,5,null] -> [2,4,1,5,3]."""
    sol = Solution()
    root = build_tree([1, 2, 3, None, 4, 5, None])
    result_rec = sol.inorderTraversalRecursive(root)
    result_iter = sol.inorderTraversalIterative(root)
    assert_equal(result_rec, [2, 4, 1, 5, 3])
    assert_equal(result_iter, [2, 4, 1, 5, 3])


def test_example3():
    """Example 3: [] -> []."""
    sol = Solution()
    root = build_tree([])
    result_rec = sol.inorderTraversalRecursive(root)
    result_iter = sol.inorderTraversalIterative(root)
    assert_equal(result_rec, [])
    assert_equal(result_iter, [])


if __name__ == "__main__":
    run_tests()
