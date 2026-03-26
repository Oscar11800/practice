from neetcode75.test_runner import assert_equal, run_tests

"""
Implement Trie (Prefix Tree)
Medium

A prefix tree (also known as a trie) is a tree data structure used to efficiently store and retrieve keys in a set of strings. Some applications of this data structure include auto-complete and spell checker systems.

Implement the PrefixTree class:

PrefixTree() Initializes the prefix tree object.
void insert(String word) Inserts the string word into the prefix tree.
boolean search(String word) Returns true if the string word is in the prefix tree (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

Example 1:
Input:
["Trie", "insert", "dog", "search", "dog", "search", "do", "startsWith", "do", "insert", "do", "search", "do"]
Output:
[null, null, true, false, true, null, true]

Constraints:
1 <= word.length, prefix.length <= 1000
word and prefix are made up of lowercase English letters
"""


class PrefixTree:
    def __init__(self):
        raise NotImplementedError

    def insert(self, word: str) -> None:
        raise NotImplementedError

    def search(self, word: str) -> bool:
        raise NotImplementedError

    def startsWith(self, prefix: str) -> bool:
        raise NotImplementedError


def test_example():
    tree = PrefixTree()
    tree.insert("dog")
    assert_equal(tree.search("dog"), True)
    assert_equal(tree.search("do"), False)
    assert_equal(tree.startsWith("do"), True)
    tree.insert("do")
    assert_equal(tree.search("do"), True)


# Run: python3 -m neetcode75.tries.prefix_tree
if __name__ == "__main__":
    run_tests()
