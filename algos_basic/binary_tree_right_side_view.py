from typing import Optional
from test_runner import assert_equal, run_tests
from collections import deque

'''
199. Binary Tree Right Side View

You are given the root of a binary tree. Return only the values of the nodes that are
visible from the right side of the tree, ordered from top to bottom.

Example 1:
  Input: root = [1,2,3,null,4,null,5]
  Output: [1,3,5]

Example 2:
  Input: root = [1,2,3,4,null,null,null,5]
  Output: [1,3,4,5]

Example 3:
  Input: root = [1,null,2]
  Output: [1,2]

Example 4:
  Input: root = []
  Output: []
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        """
        Return values of nodes visible from the right side (top to bottom).

        :param root: Root of the binary tree.
        :return: List of right-side view values.
        """
        if not root: 
            return []

        rtn = []
        queue = deque()
        queue.append(root)
        while(queue):
            level_len = len(queue)
            for i in range(level_len):
                root = queue.popleft()
                if i == level_len-1:
                    rtn.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
        return rtn


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
    """Example 1: [1,2,3,null,4,null,5] -> [1,3,5]."""
    sol = Solution()
    root = build_tree([1, 2, 3, None, 4, None, 5])
    assert_equal(sol.rightSideView(root), [1, 3, 5])


def test_example2():
    """Example 2: [1,2,3,4,null,null,null,5] -> [1,3,4,5]."""
    sol = Solution()
    root = build_tree([1, 2, 3, 4, None, None, None, 5])
    assert_equal(sol.rightSideView(root), [1, 3, 4, 5])


def test_example3():
    """Example 3: [1,null,2] -> [1,2]."""
    sol = Solution()
    root = build_tree([1, None, 2])
    assert_equal(sol.rightSideView(root), [1, 2])


def test_example4():
    """Example 4: [] -> []."""
    sol = Solution()
    root = build_tree([])
    assert_equal(sol.rightSideView(root), [])


if __name__ == "__main__":
    run_tests()
