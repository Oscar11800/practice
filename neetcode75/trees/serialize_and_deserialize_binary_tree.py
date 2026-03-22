from neetcode75.test_runner import assert_equal, run_tests
from typing import Optional

"""
Serialize and Deserialize Binary Tree
Hard

Implement an algorithm to serialize and deserialize a binary tree.

Serialization is the process of converting an in-memory structure into a
sequence of bits so that it can be stored or sent across a network to be
reconstructed later in another computer environment.

You just need to ensure that a binary tree can be serialized to a string and
this string can be deserialized to the original tree structure. There is no
additional restriction on how your serialization/deserialization algorithm
should work.

Example 1:
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Example 2:
Input: root = []
Output: []

Constraints:
0 <= The number of nodes in the tree <= 1000
-1000 <= Node.val <= 1000
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        rtn = []
        def dfs(node):
            if not node:
                rtn.append("#,")
                return
            rtn.append(f"{node.val},")
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ''.join(rtn)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.counter = 0
        vals = data.split(",")[:-1]
        def dfs():
            if vals[self.counter] == '#':
                self.counter += 1
                return None
            node = TreeNode(int((vals[self.counter])))
            self.counter += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()

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


def tree_to_list(root):
    if not root:
        return []
    result, queue = [], [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result


def test_example1():
    codec = Codec()
    root = build_tree([1,2,3,None,None,4,5])
    assert_equal(tree_to_list(codec.deserialize(codec.serialize(root))), [1,2,3,None,None,4,5])


def test_example2():
    codec = Codec()
    assert_equal(tree_to_list(codec.deserialize(codec.serialize(None))), [])


# Run: python3 -m neetcode75.trees.serialize_and_deserialize_binary_tree
if __name__ == "__main__":
    run_tests()
