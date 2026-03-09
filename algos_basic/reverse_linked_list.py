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
        pass

# ========== TESTS ==========
sol = Solution()

def test1():
    input = [0,1,2,3]
    output = [3,2,1,0]
    result = sol.reverseList(input)
    assert_equal(result, output)



def test2():
    input = []
    output = []
    result = sol.reverseList(input)
    assert_equal(result, output)

if __name__ == "__main__":
    run_tests()