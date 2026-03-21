from neetcode75.test_runner import assert_equal, run_tests

"""
Lowest Common Ancestor in Binary Search Tree
Medium

Given a binary search tree (BST) where all node values are unique, and two
nodes from the tree p and q, return the lowest common ancestor (LCA) of the
two nodes.

The lowest common ancestor between two nodes p and q is the lowest node in a
tree T such that both p and q are descendants. The ancestor is allowed to be
a descendant of itself.

Example 1:
Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 8
Output: 5

Example 2:
Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 4
Output: 3
Explanation: The LCA of nodes 3 and 4 is 3, since a node can be a descendant
of itself.

Constraints:
2 <= The number of nodes in the tree <= 100
-100 <= Node.val <= 100
p != q
p and q will both exist in the BST
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        raise NotImplementedError


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


def find_node(root, val):
    if not root:
        return None
    if root.val == val:
        return root
    return find_node(root.left, val) or find_node(root.right, val)


def test_example1():
    sol = Solution()
    root = build_tree([5,3,8,1,4,7,9,None,2])
    assert_equal(sol.lowestCommonAncestor(root, find_node(root, 3), find_node(root, 8)).val, 5)


def test_example2():
    sol = Solution()
    root = build_tree([5,3,8,1,4,7,9,None,2])
    assert_equal(sol.lowestCommonAncestor(root, find_node(root, 3), find_node(root, 4)).val, 3)


# Run: python3 -m neetcode75.trees.lowest_common_ancestor_in_binary_search_tree
if __name__ == "__main__":
    run_tests()
