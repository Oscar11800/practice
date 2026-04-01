from test_runner import assert_equal, run_tests

"""
Maximum Value of Expression

Given a non-empty string puzzle consisting of single digits and operators (+, -),
return the maximum value that can be evaluated from the puzzle.

Valid expression rules:
- Starts from a number
- Only goes left to right (no operator precedence)
- No changing direction
- Final expression doesn't have consecutive operators (e.g., "3+-2" is invalid)
- Final expression doesn't have consecutive numbers (e.g., "3+4 4" is invalid)

Example 1:
Input: puzzle = "1-1"
Output: 1

Example 2:
Input: puzzle = "1+2+3"
Output: 6
"""


def solution(puzzle):
    curr = int(puzzle[0])
    max_val = curr
    
    i = 1
    while i < len(puzzle):
        op = puzzle[i]
        i += 1
        num = int(puzzle[i])
        i += 1
        
        if op == '+':
            curr = curr + num
        else:
            curr = curr - num
        
        max_val = max(max_val, curr)
        
        if curr < 0:
            curr = 0
    
    return max_val        


def test_example1():
    sol = solution("1-1")
    assert_equal(sol, 1)


def test_example2():
    sol = solution("1+2+3")
    assert_equal(sol, 6)


# Run: python3 -m neetcode75.specific.max_expression_value
if __name__ == "__main__":
    run_tests()
