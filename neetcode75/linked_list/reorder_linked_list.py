from __future__ import annotations

from typing import Optional
from neetcode75.test_runner import assert_equal, run_tests

"""
Reorder Linked List
Medium

You are given the head of a singly linked-list.

The positions of a linked list of length = 7 for example, can initially be
represented as:
[0, 1, 2, 3, 4, 5, 6]

Reorder the nodes of the linked list to be in the following order:
[0, 6, 1, 5, 2, 4, 3]

Notice that in the general case for a list of length = n the nodes are
reordered to be in the following order:
[0, n-1, 1, n-2, 2, n-3, ...]

You may not modify the values in the list's nodes, but instead you must reorder
the nodes themselves.

Example 1:
Input: head = [2,4,6,8]
Output: [2,8,4,6]

Example 2:
Input: head = [2,4,6,8,10]
Output: [2,10,4,8,6]

Constraints:
1 <= Length of the list <= 1000.
1 <= Node.val <= 1000
"""


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        raise NotImplementedError


def build_linked_list(values: list[int]) -> Optional[ListNode]:
    if not values:
        return None

    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def linked_list_to_list(head: Optional[ListNode]) -> list[int]:
    out = []
    curr = head
    while curr:
        out.append(curr.val)
        curr = curr.next
    return out


def test_example1():
    sol = Solution()
    head = build_linked_list([2, 4, 6, 8])
    sol.reorderList(head)
    assert_equal(linked_list_to_list(head), [2, 8, 4, 6])


def test_example2():
    sol = Solution()
    head = build_linked_list([2, 4, 6, 8, 10])
    sol.reorderList(head)
    assert_equal(linked_list_to_list(head), [2, 10, 4, 8, 6])


def test_single_node():
    sol = Solution()
    head = build_linked_list([7])
    sol.reorderList(head)
    assert_equal(linked_list_to_list(head), [7])


# Run: python3 -m neetcode75.linked_list.reorder_linked_list
if __name__ == "__main__":
    run_tests()
