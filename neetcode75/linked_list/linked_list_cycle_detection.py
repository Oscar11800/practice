from __future__ import annotations

from typing import Optional
from neetcode75.test_runner import assert_equal, run_tests

"""
Linked List Cycle Detection
Easy

Given the beginning of a linked list head, return true if there is a cycle in
the linked list. Otherwise, return false.

There is a cycle in a linked list if at least one node in the list can be
visited again by following the next pointer.

Internally, index determines the index of the beginning of the cycle, if it
exists. The tail node of the list will set its next pointer to the index-th
node. If index = -1, then the tail node points to null and no cycle exists.

Note: index is not given to you as a parameter.

Example 1:
Input: head = [1,2,3,4], index = 1
Output: true

Example 2:
Input: head = [1,2], index = -1
Output: false

Constraints:
0 <= Length of the list <= 1000.
-1000 <= Node.val <= 1000
index is -1 or a valid index in the linked list.
"""


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        raise NotImplementedError


def build_linked_list_with_cycle(values: list[int], index: int) -> Optional[ListNode]:
    if not values:
        return None

    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    if index != -1:
        nodes[-1].next = nodes[index]

    return nodes[0]


def test_example1():
    sol = Solution()
    head = build_linked_list_with_cycle([1, 2, 3, 4], 1)
    assert_equal(sol.hasCycle(head), True)


def test_example2():
    sol = Solution()
    head = build_linked_list_with_cycle([1, 2], -1)
    assert_equal(sol.hasCycle(head), False)


def test_empty_list():
    sol = Solution()
    assert_equal(sol.hasCycle(None), False)


# Run: python3 -m neetcode75.linked_list.linked_list_cycle_detection
if __name__ == "__main__":
    run_tests()
