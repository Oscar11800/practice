from typing import Optional
from test_runner import assert_equal, run_tests

'''
112. Path Sum

You are given the root of a binary tree and an integer targetSum. Return true if the tree
has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Example 1:
  Input: root = [1,2,3], targetSum = 3
  Output: true
  Explanation: The root-to-leaf path with the target sum is 1 -> 2.

Example 2:
  Input: root = [-15,10,20,null,null,15,5,-5], targetSum = 15
  Output: true
  Explanation: The root-to-leaf path with the target sum is -15 -> 20 -> 15 -> -5.

Example 3:
  Input: root = [1,1,0,1], targetSum = 2
  Output: false

Constraints:
  0 <= number of nodes <= 5000
  -1000 <= Node.val <= 1000
  -1000 <= targetSum <= 1000
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    #     """
    #     Return true if any root-to-leaf path sums to targetSum.

    #     :param root: Root of the binary tree.
    #     :param targetSum: Target sum for a root-to-leaf path.
    #     :return: True if such a path exists, False otherwise.
    #     """
    #     if not root:
    #         return False
    #     stack = [(root, root.val)]
    #     while stack:
    #         node, running_sum = stack.pop()
    #         if running_sum == targetSum and not node.left and not node.right:
    #             return True
    #         if node.right:
    #             stack.append((node.right, running_sum + node.right.val))
    #         if node.left:
    #             stack.append((node.left, running_sum + node.left.val))
    #     return False

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        Return true if any root-to-leaf path sums to targetSum.

        :param root: Root of the binary tree.
        :param targetSum: Target sum for a root-to-leaf path.
        :return: True if such a path exists, False otherwise.
        """
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == targetSum
        remaining = targetSum - root.val
        return self.hasPathSum(root.left, remaining) or self.hasPathSum(root.right, remaining)
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
    """Example 1: [1,2,3], targetSum=3 -> true (path 1->2)."""
    sol = Solution()
    root = build_tree([1, 2, 3])
    assert_equal(sol.hasPathSum(root, 3), True)


def test_example2():
    """Example 2: [-15,10,20,null,null,15,5,-5], targetSum=15 -> true."""
    sol = Solution()
    root = build_tree([-15, 10, 20, None, None, 15, 5, -5])
    assert_equal(sol.hasPathSum(root, 15), True)


def test_example3():
    """Example 3: [1,1,0,1], targetSum=2 -> false."""
    sol = Solution()
    root = build_tree([1, 1, 0, 1])
    assert_equal(sol.hasPathSum(root, 2), False)


if __name__ == "__main__":
    run_tests()