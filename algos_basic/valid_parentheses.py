from test_runner import assert_equal, run_tests

'''
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.
'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openers = "[{("
        for c in s:
            if c in openers:
                stack.append(c)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if c == ']':
                    if top != '[':
                        return False
                elif c == ')':
                    if top != '(':
                        return False
                else:
                    if top != '{':
                        return False
        return not stack

sol = Solution()

def test1():
    input = "[]"
    output = True
    result = sol.isValid(input)
    assert_equal(result, output)



def test2():
    input = "([{}])"
    output = True
    result = sol.isValid(input)
    assert_equal(result, output)

def test3():
    input = "[(])"
    output = False
    result = sol.isValid(input)
    assert_equal(result, output)

if __name__ == "__main__":
    run_tests()