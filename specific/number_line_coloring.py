from test_runner import assert_equal, run_tests

"""
Number Line Coloring

Given a number line represented by [0, length-1] 
and a list of queries that determine how to color coordinates.

Each query is in format [coordinate, color]. 
Color the coordinate with the given color (overwrite existing color).

After each query, record the number of consecutive pairs of coordinates
which have the same color on the number line.

Return an array of length equal to queries.length with these counts.

Example:
Input: length = 7, queries = [[1,2],[0,2],[3,5],[3,2],[2,2],[6,1],[1,3]]
Output: [0, 1, 1, 1, 3, 3, 1]
"""


def solution(length, queries):
    color_arr = [-1] * length
    rtn = [] 
    for query in queries:
        idx = query[0]
        color = query[1]
        color_arr[idx] = color
        rtn.append(countConsecutive(color_arr))
    return rtn
    
def countConsecutive(arr):
    count = 0
    for i in range(len(arr) - 1):
        if arr[i] == arr[i+1] and arr[i] != -1:
            count += 1 
    return count
    

def test_example():
    sol = solution(
        7, [[1, 2], [0, 2], [3, 5], [3, 2], [2, 2], [6, 1], [1, 3]]
    )
    assert_equal(sol, [0, 1, 1, 1, 3, 3, 1])


# Run: python3 -m neetcode75.specific.number_line_coloring
if __name__ == "__main__":
    run_tests()
