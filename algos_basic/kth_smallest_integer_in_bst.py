from typing import Optional
from test_runner import assert_equal, run_tests

'''
230. Kth Smallest Element in a BST

Given the root of a binary search tree and an integer k, return the kth smallest value
(1-indexed) of all the values of the nodes in the tree.

A BST satisfies:
- Left subtree: keys less than node's key
- Right subtree: keys greater than node's key
- Both subtrees are also BSTs

Example 1:
  Input: root = [2,1,3], k = 1
  Output: 1

Example 2:
  Input: root = [4,3,5,2,null], k = 4
  Output: 5

Constraints:
  1 <= k <= number of nodes <= 1000
  0 <= Node.val <= 1000
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Return the kth smallest value (1-indexed) in the BST.

        :param root: Root of the BST.
        :param k: 1-indexed position (1 = smallest).
        :return: The kth smallest value.
        """
        counter = 1
        curr = root
        stack = []
        ret = 0

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            ret = curr.val
            if counter == k:
                return ret
            counter += 1
            curr = curr.right
        return ret
            


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
    """Example 1: [2,1,3], k=1 -> 1."""
    sol = Solution()
    root = build_tree([2, 1, 3])
    assert_equal(sol.kthSmallest(root, 1), 1)


def test_example2():
    """Example 2: [4,3,5,2,null], k=4 -> 5."""
    sol = Solution()
    root = build_tree([4, 3, 5, 2, None])
    assert_equal(sol.kthSmallest(root, 4), 5)


if __name__ == "__main__":
    run_tests()
