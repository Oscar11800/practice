# Definition for singly-linked list.

from typing import Optional
from test_runner import assert_equal, run_tests
'''
Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

# ========== TESTS ==========
sol = Solution()

def test1():
    # Create linked list: 0 -> 1 -> 2 -> 3 -> None
    node0 = ListNode(0)
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node0.next = node1
    node1.next = node2
    node2.next = node3
    
    # Reverse it
    result_head = sol.reverseList(node0)
    
    # Convert result to list for comparison
    result_list = []
    curr = result_head
    while curr:
        result_list.append(curr.val)
        curr = curr.next
    
    assert_equal(result_list, [3, 2, 1, 0])


def test2():
    # Empty list
    result_head = sol.reverseList(None)
    
    # Convert result to list
    result_list = []
    curr = result_head
    while curr:
        result_list.append(curr.val)
        curr = curr.next
    
    assert_equal(result_list, [])


def test3():
    # Single node: 5 -> None
    node = ListNode(5)
    
    result_head = sol.reverseList(node)
    
    # Convert result to list
    result_list = []
    curr = result_head
    while curr:
        result_list.append(curr.val)
        curr = curr.next
    
    assert_equal(result_list, [5])

if __name__ == "__main__":
    run_tests()