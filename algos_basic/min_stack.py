from test_runner import assert_equal, run_tests

'''
Design a stack class that supports the push, pop, top, and getMin operations.

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
Each function should run in 
O(1) time.
'''
class MinStack:
    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mins:
            self.mins.append(val)
        else:
            current_min = self.getMin()
            if val < current_min: 
                self.mins.append(val)
            else:
                self.mins.append(current_min)

    def pop(self) -> None:
        self.stack.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]


# ============== Tests ===============
def test1():
    """
    Example case:
    MinStack minStack = new MinStack();
    minStack.push(1);
    minStack.push(2);
    minStack.push(0);
    minStack.getMin(); // return 0
    minStack.pop();
    minStack.top();    // return 2
    minStack.getMin(); // return 1
    """
    minStack = MinStack()
    
    minStack.push(1)
    minStack.push(2)
    minStack.push(0)
    
    assert_equal(minStack.getMin(), 0)
    
    minStack.pop()
    
    assert_equal(minStack.top(), 2)
    assert_equal(minStack.getMin(), 1)


def test2():
    """Test with single element"""
    minStack = MinStack()
    minStack.push(5)
    assert_equal(minStack.top(), 5)
    assert_equal(minStack.getMin(), 5)


def test3():
    """Test with duplicate minimums"""
    minStack = MinStack()
    minStack.push(2)
    minStack.push(1)
    minStack.push(3)
    minStack.push(1)  # Duplicate min
    
    assert_equal(minStack.getMin(), 1)
    minStack.pop()  # Remove one of the 1s
    assert_equal(minStack.getMin(), 1)  # Should still be 1
    assert_equal(minStack.top(), 3)


def test4():
    """Test with negative numbers"""
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    
    assert_equal(minStack.getMin(), -3)
    minStack.pop()
    assert_equal(minStack.top(), 0)
    assert_equal(minStack.getMin(), -2)


def test5():
    """Test multiple pops and min updates"""
    minStack = MinStack()
    minStack.push(5)
    minStack.push(3)
    minStack.push(4)
    minStack.push(2)
    minStack.push(6)
    
    assert_equal(minStack.getMin(), 2)
    minStack.pop()  # Remove 6
    assert_equal(minStack.getMin(), 2)
    minStack.pop()  # Remove 2
    assert_equal(minStack.getMin(), 3)
    minStack.pop()  # Remove 4
    assert_equal(minStack.getMin(), 3)
    minStack.pop()  # Remove 3
    assert_equal(minStack.getMin(), 5)
    assert_equal(minStack.top(), 5)

if __name__ == "__main__":
    run_tests()