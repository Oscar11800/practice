from test_runner import assert_equal, run_tests
import math
'''
875. Koko Eating Bananas

You are given an integer array piles where piles[i] is the number of bananas in the ith
pile. You are also given an integer h, which represents the number of hours you have to
eat all the bananas.

You may decide your bananas-per-hour eating rate k. Each hour, you may choose a pile of
bananas and eat k bananas from that pile. If the pile has less than k bananas, you may
finish eating the pile but you cannot eat from another pile in the same hour.

Return the minimum integer k such that you can eat all the bananas within h hours.

Example 1:
  Input: piles = [1,4,3,2], h = 9
  Output: 2
  Explanation: With k=2, you can eat all in 6 hours. With k=1, you need 10 hours (>9).

Example 2:
  Input: piles = [25,10,23,4], h = 4
  Output: 25

Constraints:
  1 <= piles.length <= 1,000
  piles.length <= h <= 1,000,000
  1 <= piles[i] <= 1,000,000,000
'''


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        """
        Find the minimum eating rate k to finish all bananas in h hours.

        :param piles: Number of bananas in each pile.
        :param h: Hours available.
        :return: Minimum k (bananas per hour).
        """
        left, right = 1, max(piles)
        while left < right:
          mid = (left + right)//2
          totalh = sum(map(lambda x: math.ceil(x/mid), piles))
          if totalh > h:
            left = mid + 1
          else:
            right = mid

        return left


# ========== TESTS ==========

def test_example1():
    """Example 1: piles=[1,4,3,2], h=9 -> 2."""
    sol = Solution()
    assert_equal(sol.minEatingSpeed([1, 4, 3, 2], 9), 2)


def test_example2():
    """Example 2: piles=[25,10,23,4], h=4 -> 25."""
    sol = Solution()
    assert_equal(sol.minEatingSpeed([25, 10, 23, 4], 4), 25)


if __name__ == "__main__":
    run_tests()
