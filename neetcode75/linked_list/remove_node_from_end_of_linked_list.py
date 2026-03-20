from __future__ import annotations

from typing import Optional
from neetcode75.test_runner import assert_equal, run_tests

"""
Remove Node From End of Linked List

You are given the beginning of a linked list head, and an integer n.

Remove the nth node from the end of the list and return the beginning of the
list.

Example 1:
Input: head = [1,2,3,4], n = 2
Output: [1,2,4]

Example 2:
Input: head = [5], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 2
Output: [2]

Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None
        length = 0
        end = head
        while end is not None:
            length += 1
            end = end.next
        
        dummy = ListNode(0, head)
        prev = dummy
        curr = head
        count = 0

        while count < (length - n):
            prev = curr
            curr = curr.next
            count += 1
            
        prev.next = curr.next
        curr.next = None
        return dummy.next
        


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
    head = build_linked_list([1, 2, 3, 4])
    new_head = sol.removeNthFromEnd(head, 2)
    assert_equal(linked_list_to_list(new_head), [1, 2, 4])


def test_example2():
    sol = Solution()
    head = build_linked_list([5])
    new_head = sol.removeNthFromEnd(head, 1)
    assert_equal(linked_list_to_list(new_head), [])


def test_example3():
    sol = Solution()
    head = build_linked_list([1, 2])
    new_head = sol.removeNthFromEnd(head, 2)
    assert_equal(linked_list_to_list(new_head), [2])


# Run: python3 -m neetcode75.linked_list.remove_node_from_end_of_linked_list
if __name__ == "__main__":
    run_tests()