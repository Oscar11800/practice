from typing import Optional
import heapq
from test_runner import assert_equal, run_tests

'''
23. Merge k Sorted Lists

You are given an array of k linked lists lists, where each linked list is sorted in
ascending order.

Merge all the linked lists into one sorted linked list and return it.

Example 1:
  Input: lists = [[1,2,4],[1,3,5],[3,6]]
  Output: [1,1,2,3,3,4,5,6]

Example 2:
  Input: lists = []
  Output: []

Example 3:
  Input: lists = [[]]
  Output: []
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Merge k sorted linked lists into one sorted linked list.

        :param lists: Array of linked list heads (each list is sorted ascending).
        :return: Head of the merged sorted linked list.
        """
        heap = []
        id = 0
        # initialize the heap
        for l in lists:  # noqa: E741
            if l:
                heapq.heappush(heap, (l.val, id, l))
                id += 1
        dummy = ListNode()
        curr = dummy
        while heap:
            val, _, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, id, node.next))
            id += 1
        return dummy.next



# ========== HELPERS ==========

def list_to_linked_list(arr: list[int]) -> Optional[ListNode]:
    """Convert [1,2,4] -> ListNode(1)->ListNode(2)->ListNode(4)->None."""
    if not arr:
        return None
    dummy = ListNode()
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


def linked_list_to_list(head: Optional[ListNode]) -> list[int]:
    """Convert linked list to list for easy comparison."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# ========== TESTS ==========

def test_example1():
    """Example 1: [[1,2,4],[1,3,5],[3,6]] -> [1,1,2,3,3,4,5,6]."""
    sol = Solution()
    lists = [
        list_to_linked_list([1, 2, 4]),
        list_to_linked_list([1, 3, 5]),
        list_to_linked_list([3, 6]),
    ]
    result = sol.mergeKLists(lists)
    assert_equal(linked_list_to_list(result), [1, 1, 2, 3, 3, 4, 5, 6])


def test_example2():
    """Example 2: [] -> []."""
    sol = Solution()
    result = sol.mergeKLists([])
    assert_equal(linked_list_to_list(result), [])


def test_example3():
    """Example 3: [[]] -> []."""
    sol = Solution()
    lists = [list_to_linked_list([])]
    result = sol.mergeKLists(lists)
    assert_equal(linked_list_to_list(result), [])


if __name__ == "__main__":
    run_tests()
