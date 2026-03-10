from test_runner import assert_equal, run_tests
# NOTE: This is only partially successful. Needs major revisions
'''
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next.
val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, 
you will need one more attribute prev to indicate the previous node in the linked list.
Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. 
    After the insertion, the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. 
    If index equals the length of the linked list, the node will be appended to the end of the linked list. 
    If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
'''
class MyLinkedList(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0:
            return -1
        if not self.next and self.val == 0:  # Empty list
            return -1
        curr = self
        for _ in range(index):
            if not curr or not curr.next:
                return -1
            curr = curr.next
        return curr.val if curr else -1
        

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.next and self.val == 0:  # Empty list
            self.val = val
            self.next = None
        else:
            copy = MyLinkedList(self.val, self.next)
            self.val = val
            self.next = copy
        

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.next and self.val == 0:  # Empty list
            self.val = val
            self.next = None
            return
        curr = self
        while curr.next:
            curr = curr.next
        curr.next = MyLinkedList(val, None)
        

    def addAtIndex(self, index, val):
        if index < 0:
            return
        if index == 0:
            if not self.next and self.val == 0:  # Empty list
                self.val = val
                self.next = None
                return
            copy = MyLinkedList(self.val, self.next)
            self.val = val
            self.next = copy
            return
        # index > 0: invalid if list is empty
        if not self.next and self.val == 0:
            return
        curr = self
        # index > 0: don't use empty check - [0] is a valid 1-element list
        curr = self
        for _ in range(index):
            if not curr:
                return
            curr = curr.next
        if curr is None:
            # Index equals length - append at tail
            prev = self
            while prev.next:
                prev = prev.next
            prev.next = MyLinkedList(val, None)
        else:
            # Insert before curr
            prev = self
            while prev.next != curr:
                prev = prev.next
            prev.next = MyLinkedList(val, curr)
        

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0:
            return
        if not self.next and self.val == 0:  # Empty list
            return
        if index == 0:
            if self.next:
                self.val = self.next.val  # Get val FIRST
                self.next = self.next.next  # Then update next
            else:
                self.val = 0
                self.next = None
            return
        curr = self
        for _ in range(index):
            if not curr or not curr.next:
                return  # Invalid index
            curr = curr.next
        if not curr:
            return
        prev = self
        while prev.next != curr:
            prev = prev.next
        prev.next = curr.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

# ========== TESTS ==========
def test1():
    """
    Example case from problem description
    """
    myLinkedList = MyLinkedList()
    
    # Initial state - empty list
    assert_equal(myLinkedList.get(0), -1)  # Invalid index
    
    # Add at head
    myLinkedList.addAtHead(1)  # List: 1
    assert_equal(myLinkedList.get(0), 1)
    
    # Add at tail
    myLinkedList.addAtTail(3)  # List: 1 -> 3
    assert_equal(myLinkedList.get(0), 1)
    assert_equal(myLinkedList.get(1), 3)
    
    # Add at index
    myLinkedList.addAtIndex(1, 2)  # List: 1 -> 2 -> 3
    assert_equal(myLinkedList.get(0), 1)
    assert_equal(myLinkedList.get(1), 2)
    assert_equal(myLinkedList.get(2), 3)
    
    # Get value at index 1
    result1 = myLinkedList.get(1)
    assert_equal(result1, 2)
    
    # Delete at index
    myLinkedList.deleteAtIndex(1)  # List: 1 -> 3
    assert_equal(myLinkedList.get(0), 1)
    assert_equal(myLinkedList.get(1), 3)
    assert_equal(myLinkedList.get(2), -1)  # Invalid index
    
    # Get value at index 1 after deletion
    result2 = myLinkedList.get(1)
    assert_equal(result2, 3)
def test2():
    """Test addAtHead multiple times"""
    myLinkedList = MyLinkedList()
    
    myLinkedList.addAtHead(3)
    myLinkedList.addAtHead(2)
    myLinkedList.addAtHead(1)  # List: 1 -> 2 -> 3
    
    assert_equal(myLinkedList.get(0), 1)
    assert_equal(myLinkedList.get(1), 2)
    assert_equal(myLinkedList.get(2), 3)
def test3():
    """Test addAtTail multiple times"""
    myLinkedList = MyLinkedList()
    
    myLinkedList.addAtTail(1)
    myLinkedList.addAtTail(2)
    myLinkedList.addAtTail(3)  # List: 1 -> 2 -> 3
    
    assert_equal(myLinkedList.get(0), 1)
    assert_equal(myLinkedList.get(1), 2)
    assert_equal(myLinkedList.get(2), 3)
def test4():
    """Test addAtIndex at various positions"""
    myLinkedList = MyLinkedList()
    
    myLinkedList.addAtHead(1)
    myLinkedList.addAtTail(3)
    myLinkedList.addAtIndex(1, 2)  # List: 1 -> 2 -> 3
    
    # Add at index 0 (head)
    myLinkedList.addAtIndex(0, 0)  # List: 0 -> 1 -> 2 -> 3
    assert_equal(myLinkedList.get(0), 0)
    
    # Add at index equal to length (tail)
    myLinkedList.addAtIndex(4, 4)  # List: 0 -> 1 -> 2 -> 3 -> 4
    assert_equal(myLinkedList.get(4), 4)
    
    # Invalid index (too large)
    myLinkedList.addAtIndex(10, 10)  # Should not add
    assert_equal(myLinkedList.get(5), -1)
def test5():
    """Test deleteAtIndex edge cases"""
    myLinkedList = MyLinkedList()
    
    myLinkedList.addAtHead(1)
    myLinkedList.addAtTail(2)
    myLinkedList.addAtTail(3)  # List: 1 -> 2 -> 3
    
    # Delete middle
    myLinkedList.deleteAtIndex(1)  # List: 1 -> 3
    assert_equal(myLinkedList.get(0), 1)
    assert_equal(myLinkedList.get(1), 3)
    
    # Delete head
    myLinkedList.deleteAtIndex(0)  # List: 3
    assert_equal(myLinkedList.get(0), 3)
    
    # Delete tail
    myLinkedList.deleteAtIndex(0)  # List: empty
    assert_equal(myLinkedList.get(0), -1)
    
    # Delete invalid index
    myLinkedList.deleteAtIndex(0)  # Should not crash
    assert_equal(myLinkedList.get(0), -1)
def test6():
    """Test get with invalid indices"""
    myLinkedList = MyLinkedList()
    
    assert_equal(myLinkedList.get(-1), -1)  # Negative index
    assert_equal(myLinkedList.get(0), -1)   # Empty list
    
    myLinkedList.addAtHead(1)
    assert_equal(myLinkedList.get(0), 1)
    assert_equal(myLinkedList.get(1), -1)   # Out of bounds
    assert_equal(myLinkedList.get(-1), -1)  # Negative index
def test7():
    """Test complex sequence"""
    myLinkedList = MyLinkedList()
    
    # Build list: 7 -> 2 -> 1
    myLinkedList.addAtHead(1)
    myLinkedList.addAtHead(2)
    myLinkedList.addAtHead(7)
    
    # Add 0 at index 1: 7 -> 0 -> 2 -> 1
    myLinkedList.addAtIndex(1, 0)
    assert_equal(myLinkedList.get(1), 0)
    
    # Delete index 2: 7 -> 0 -> 1
    myLinkedList.deleteAtIndex(2)
    assert_equal(myLinkedList.get(2), 1)
    
    # Add 4 at tail: 7 -> 0 -> 1 -> 4
    myLinkedList.addAtTail(4)
    assert_equal(myLinkedList.get(3), 4)
if __name__ == "__main__":
    run_tests()