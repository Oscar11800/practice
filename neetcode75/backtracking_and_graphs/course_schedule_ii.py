from typing import List
from neetcode75.test_runner import assert_equal, run_tests

"""
Course Schedule II
Medium

You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.

Return a valid ordering of courses you can take to finish all courses. If there are many valid answers, return any of them. If it's not possible to finish all courses, return an empty array.

Example 1:
Input: numCourses = 3, prerequisites = [[1,0]]
Output: [0,1,2]

Example 2:
Input: numCourses = 3, prerequisites = [[0,1],[1,2],[2,0]]
Output: []

Constraints:
1 <= numCourses <= 1000
0 <= prerequisites.length <= 1000
All prerequisite pairs are unique.
"""


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        raise NotImplementedError


def test_example1():
    sol = Solution()
    result = sol.findOrder(3, [[1, 0]])
    assert_equal(len(result), 3)
    assert result.index(0) < result.index(1)


def test_example2():
    sol = Solution()
    assert_equal(sol.findOrder(3, [[0, 1], [1, 2], [2, 0]]), [])


def test_no_prerequisites():
    sol = Solution()
    assert_equal(sol.findOrder(2, []), [0, 1])


# Run: python3 -m neetcode75.backtracking_and_graphs.course_schedule_ii
if __name__ == "__main__":
    run_tests()
