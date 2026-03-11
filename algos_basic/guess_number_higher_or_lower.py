from test_runner import assert_equal, run_tests

'''
374. Guess Number Higher or Lower

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or
lower than your guess.

You call a pre-defined API guess(num), which returns three possible results:
  -1: Your guess is higher than the number I picked (num > pick)
   1: Your guess is lower than the number I picked (num < pick)
   0: Your guess is equal to the number I picked (num == pick)

Return the number that I picked.

Example 1:
  Input: n = 5, pick = 3
  Output: 3

Example 2:
  Input: n = 15, pick = 10
  Output: 10

Example 3:
  Input: n = 1, pick = 1
  Output: 1
'''

# For testing: set _pick before each test; guess() uses it
_pick = 0


def guess(num: int) -> int:
    """Pre-defined API. Returns -1 if num > pick, 1 if num < pick, 0 if num == pick."""
    if num == _pick:
        return 0
    return -1 if num > _pick else 1


class Solution:
    def guessNumber(self, n: int) -> int:
        """
        Guess the picked number between 1 and n using the guess() API.

        :param n: Upper bound of the range (1 to n).
        :return: The picked number.
        """
        left, right = 0, n
        mid = n // 2

        while left <= right:
            res = guess(mid)
            if not res:
                return mid
            elif res == 1:
                left = mid + 1
                mid = (left + right) // 2
            else:
                right = mid - 1
                mid = (left + right) // 2
        return mid

# ========== TESTS ==========

def test_example1():
    """Example 1: n=5, pick=3."""
    global _pick
    _pick = 3
    sol = Solution()
    assert_equal(sol.guessNumber(5), 3)


def test_example2():
    """Example 2: n=15, pick=10."""
    global _pick
    _pick = 10
    sol = Solution()
    assert_equal(sol.guessNumber(15), 10)


def test_example3():
    """Example 3: n=1, pick=1."""
    global _pick
    _pick = 1
    sol = Solution()
    assert_equal(sol.guessNumber(1), 1)


if __name__ == "__main__":
    run_tests()
