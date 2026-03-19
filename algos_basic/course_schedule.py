from collections import defaultdict, deque
from typing import DefaultDict, List
from test_runner import assert_equal, run_tests

'''
207. Course Schedule

You are given prerequisites where prerequisites[i] = [a, b] means:
to take course a, you must first take course b.

There are numCourses courses labeled 0 to numCourses - 1.

Return true if it is possible to finish all courses, otherwise false.

Example 1:
  Input: numCourses = 2, prerequisites = [[0,1]]
  Output: true
  Explanation: take 1 first, then 0.

Example 2:
  Input: numCourses = 2, prerequisites = [[0,1],[1,0]]
  Output: false
  Explanation: cycle 0 <-> 1, impossible.

Constraints:
  1 <= numCourses <= 1000
  0 <= prerequisites.length <= 1000
  prerequisites[i].length == 2
  0 <= a, b < numCourses
  All prerequisite pairs are unique.
'''


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Return whether all courses can be completed.

        :param numCourses: Total number of courses.
        :param prerequisites: List of [a, b] prerequisite pairs.
        :return: True if possible to finish all courses, else False.
        """
        adjacency = {i: [] for i in range(numCourses)}
        indegree = {i: 0 for i in range(numCourses)}
        
        queue = deque()
        remaining_courses = numCourses
        for prereq in prerequisites:
            a, b = prereq
            adjacency[b].append(a)
            indegree[a] += 1
        for c, prereqs in indegree.items():
            if prereqs == 0:
                queue.append(c)
        
        while queue:
            print("checking")
            course = queue.popleft()
            print(course)
            remaining_courses -= 1
            if remaining_courses == 0:
                return True
            for next_class in adjacency[course]:
                indegree[next_class] -= 1
                if indegree[next_class] == 0:
                    queue.append(next_class)

        return False


# ========== TESTS ==========

def test_example1():
    """Example 1: possible."""
    sol = Solution()
    assert_equal(sol.canFinish(2, [[0, 1]]), True)


def test_example2():
    """Example 2: cycle, impossible."""
    sol = Solution()
    assert_equal(sol.canFinish(2, [[0, 1], [1, 0]]), False)


if __name__ == "__main__":
    run_tests()