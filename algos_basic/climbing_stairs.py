from test_runner import assert_equal, run_tests

'''
70. Climbing Stairs

You are given an integer n representing the number of steps to reach the top of a staircase.
You can climb with either 1 or 2 steps at a time.

Return the number of distinct ways to climb to the top of the staircase.

Example 1:
  Input: n = 2
  Output: 2
  Explanation: 1+1=2, 2=2

Example 2:
  Input: n = 3
  Output: 3
  Explanation: 1+1+1=3, 1+2=3, 2+1=3

Constraints:
  1 <= n <= 45
'''


class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Return the number of distinct ways to climb n steps (1 or 2 steps at a time).

        :param n: Number of steps to the top.
        :return: Number of distinct ways to climb.
        """
        def climb(n, memo):
            if n in memo:
                return memo[n]
            if n <= 1:
                return 1
            memo[n] = climb(n-1, memo) + climb(n-2, memo)
            return memo[n]
        return climb(n, {})

# ========== TESTS ==========

def test_example1():
    """Example 1: n=2 -> 2 ways."""
    sol = Solution()
    assert_equal(sol.climbStairs(2), 2)


def test_example2():
    """Example 2: n=3 -> 3 ways."""
    sol = Solution()
    assert_equal(sol.climbStairs(3), 3)


if __name__ == "__main__":
    run_tests()
