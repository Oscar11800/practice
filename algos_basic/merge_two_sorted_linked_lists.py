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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pass

# ========== TESTS ==========
sol = Solution()



def test1():
    list1 = [1,2,4]
    list2 = [1,3,5]
    output = [1,1,2,3,4,5]
    result = sol.reverseList(list1, list2)
    assert_equal(result, output)

def test2():
    list1 = []
    list2 = [1,2]
    output = [1,2]
    result = sol.reverseList(list1, list2)
    assert_equal(result, output)

def test3():
    list1 = []
    list2 = []
    output = []
    result = sol.reverseList(list1, list2)
    assert_equal(result, output)

if __name__ == "__main__":
    run_tests()