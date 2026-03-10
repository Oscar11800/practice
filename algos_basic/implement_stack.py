from test_runner import assert_equal, run_tests
from collections import deque
'''
Implement a last-in-first-out (LIFO) stack using only two queues.
The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.

Notes:
- You must use only standard operations of a queue: push to back, peek/pop from front, size, is empty.
- You may simulate a queue using a list or deque as long as you use only queue operations.
'''


class MyStack:
    def __init__(self):
        """Initialize two queues."""
        self.q1 = deque()
        self.q2 = deque()
        self.toggle = 0
        self.size = 0

    def push(self, x: int) -> None:
        """Push element x to the top of the stack."""
        # first move everything from q1 to q1, then push element and then push back into q1
        if not self.toggle: # q1 has stuff
            self.q2.append(x)
            while self.q1:
                self.q2.append(self.q1.popleft())
            self.toggle = 1
        else:
            self.q1.append(x)
            while self.q2:
                self.q1.append(self.q2.popleft())
            self.toggle = 0
        self.size += 1


    def pop(self) -> int:
        """Remove and return the element on top of the stack."""
        if not self.toggle:
            self.size -= 1
            return self.q1.popleft()
        else:
            self.size -= 1
            return self.q2.popleft()
        


    def top(self) -> int:
        """Return the element on top of the stack without removing it."""
        if not self.toggle:
            return self.q1[0]
        else:
            return self.q2[0]

    def empty(self) -> bool:
        """Return True if the stack is empty, False otherwise."""
        return self.size == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

# ========== TESTS ==========
# Input: ["MyStack", "push", "push", "top", "pop", "empty"]
# Args:  [[], [1], [2], [], [], []]
# Output: [null, null, null, 2, 2, false]
def test1():
    """Example: push 1, push 2, top, pop, empty"""
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    assert_equal(stack.top(), 2)
    assert_equal(stack.pop(), 2)
    assert_equal(stack.empty(), False)


if __name__ == "__main__":
    run_tests()