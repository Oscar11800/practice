# Definition for singly-linked list.

from typing import Optional
from test_runner import assert_equal, run_tests
'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

The new list should be made up of nodes from list1 and list2.
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        lp1 = list1
        lp2 = list2
        while lp1 or lp2:
            if lp1 and lp2:
                if lp1.val <= lp2.val:
                    curr.next = lp1
                    lp1 = lp1.next
                else:
                    curr.next = lp2
                    lp2 = lp2.next
            elif lp1 and not lp2:
                curr.next = lp1
                lp1 = lp1.next
            else:
                curr.next = lp2
                lp2 = lp2.next
            curr = curr.next
        return dummy.next


# ========== TESTS ==========
sol = Solution()

def test1():
    # Create list1: 1 -> 2 -> 4 -> None
    list1_node1 = ListNode(1)
    list1_node2 = ListNode(2)
    list1_node3 = ListNode(4)
    list1_node1.next = list1_node2
    list1_node2.next = list1_node3
    
    # Create list2: 1 -> 3 -> 5 -> None
    list2_node1 = ListNode(1)
    list2_node2 = ListNode(3)
    list2_node3 = ListNode(5)
    list2_node1.next = list2_node2
    list2_node2.next = list2_node3
    
    # Merge them
    result_head = sol.mergeTwoLists(list1_node1, list2_node1)
    
    # Convert result to list for comparison
    result_list = []
    curr = result_head
    while curr:
        result_list.append(curr.val)
        curr = curr.next
    
    assert_equal(result_list, [1, 1, 2, 3, 4, 5])


def test2():
    # Empty list1, list2: 1 -> 2 -> None
    list1_head = None
    
    list2_node1 = ListNode(1)
    list2_node2 = ListNode(2)
    list2_node1.next = list2_node2
    
    # Merge them
    result_head = sol.mergeTwoLists(list1_head, list2_node1)
    
    # Convert result to list
    result_list = []
    curr = result_head
    while curr:
        result_list.append(curr.val)
        curr = curr.next
    
    assert_equal(result_list, [1, 2])


def test3():
    # Both empty lists
    list1_head = None
    list2_head = None
    
    # Merge them
    result_head = sol.mergeTwoLists(list1_head, list2_head)
    
    # Convert result to list
    result_list = []
    curr = result_head
    while curr:
        result_list.append(curr.val)
        curr = curr.next
    
    assert_equal(result_list, [])
if __name__ == "__main__":
    run_tests()