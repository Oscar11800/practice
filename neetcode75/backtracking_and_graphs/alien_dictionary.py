from neetcode75.test_runner import assert_equal, run_tests
from typing import List
from collections import defaultdict, deque
"""
Alien Dictionary


There is a foreign language which uses the latin alphabet, but the order among
letters is not "a", "b", "c" ... "z" as in English.

You receive a list of non-empty strings words from the dictionary, where the
words are sorted lexicographically based on the rules of this new language.

Derive the order of letters in this language. If the order is invalid, return
an empty string. If there are multiple valid orders of letters, return any of
them.

A string a is lexicographically smaller than b if either:
- The first letter where they differ is smaller in a than in b.
- a is a prefix of b and a.length < b.length.

Example 1:
Input: ["z","o"]
Output: "zo"
Explanation: From "z" and "o", we know 'z' < 'o', so return "zo".

Example 2:
Input: ["hrn","hrf","er","enn","rfnn"]
Output: "hernf"
Explanation:
from "hrn" and "hrf", we know 'n' < 'f'
from "hrf" and "er", we know 'h' < 'e'
from "er" and "enn", we know 'r' < 'n'
from "enn" and "rfnn", we know 'e' < 'r'
so one possible solution is "hernf"

Constraints:
The input words will contain characters only from lowercase 'a' to 'z'
1 <= words.length <= 100
1 <= words[i].length <= 100
"""


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        inbound = defaultdict(int)
        edges = set()
        unique_chars = set()
        # compare adj words to create edges and inbound
        for word in words:
            for c in word:
                unique_chars.add(c)
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            j = 0
            while j < len(w1) and j < len(w2):
                if w1[j] == w2[j]:
                    j += 1
                else:
                    src = w1[j]
                    dst = w2[j]
                    if (src, dst) in edges:
                        break
                    else:
                        inbound[dst] += 1
                        edges.add((src, dst))
                        break
                    
            if j == len(w2) and len(w2) < len(w1):
                return ""
        # construct adj list
        adj = {src: [] for src in unique_chars}

        for edge in edges:
            a, b = edge
            adj[a].append(b)
        # Kahn's BFS to get order
        queue = deque()
        order = []
        # init queue with earliest char(s)
        for node in unique_chars:
            if inbound[node] == 0:
                queue.append(node)

        # process chars and get order
        while queue:
            node = queue.pop()
            order.append(node)
            for neighbor in adj[node]:
                inbound[neighbor] -= 1
                if inbound[neighbor] == 0:
                    queue.append(neighbor)
        # check for cycles
        if len(order) != len(unique_chars):
            return ""
        return ''.join(order)





def test_example1():
    sol = Solution()
    assert_equal(sol.foreignDictionary(["z","o"]), "zo")


def test_example2():
    sol = Solution()
    assert_equal(sol.foreignDictionary(["hrn","hrf","er","enn","rfnn"]), "hernf")


# Run: python3 -m neetcode75.backtracking_and_graphs.alien_dictionary
if __name__ == "__main__":
    run_tests()
