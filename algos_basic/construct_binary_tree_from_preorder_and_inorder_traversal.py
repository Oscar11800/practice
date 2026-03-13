from typing import Optional
from test_runner import assert_equal, run_tests

'''
105. Construct Binary Tree from Preorder and Inorder Traversal

You are given two integer arrays preorder and inorder.

- preorder is the preorder traversal of a binary tree
- inorder is the inorder traversal of the same tree

Both arrays are of the same size and consist of unique values. Rebuild the binary tree
from the preorder and inorder traversals and return its root.

Preorder: root → left → right
Inorder: left → root → right

Example 1:
  Input: preorder = [1,2,3,4], inorder = [2,1,3,4]
  Output: [1,2,3,null,null,null,4]

Example 2:
  Input: preorder = [1], inorder = [1]
  Output: [1]

Constraints:
  1 <= inorder.length <= 1000
  inorder.length == preorder.length
  -1000 <= preorder[i], inorder[i] <= 1000
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        """
        Rebuild the binary tree from preorder and inorder traversals.

        :param preorder: Preorder traversal (root, left, right).
        :param inorder: Inorder traversal (left, root, right).
        :return: Root of the constructed tree.
        """
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        cutoff = inorder.index(root.val)

        root.left = self.buildTree(preorder[1:1+cutoff:], inorder[0:cutoff])
        root.right = self.buildTree(preorder[1+cutoff:], inorder[cutoff+1:])
        return root


# ========== HELPERS ==========

def preorder_traversal(root: Optional[TreeNode]) -> list[int]:
    """Preorder: root → left → right."""
    if not root:
        return []
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right)


def inorder_traversal(root: Optional[TreeNode]) -> list[int]:
    """Inorder: left → root → right."""
    if not root:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)


# ========== TESTS ==========

def test_example1():
    """Example 1: preorder=[1,2,3,4], inorder=[2,1,3,4]."""
    sol = Solution()
    result = sol.buildTree([1, 2, 3, 4], [2, 1, 3, 4])
    assert_equal(preorder_traversal(result), [1, 2, 3, 4])
    assert_equal(inorder_traversal(result), [2, 1, 3, 4])


def test_example2():
    """Example 2: preorder=[1], inorder=[1]."""
    sol = Solution()
    result = sol.buildTree([1], [1])
    assert_equal(preorder_traversal(result), [1])
    assert_equal(inorder_traversal(result), [1])


if __name__ == "__main__":
    run_tests()
