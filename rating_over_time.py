from neetcode75.test_runner import assert_equal, run_tests

"""
Rating Over Time
Easy

Given a starting rating of 1500 and an array of rating changes (diffs), calculate and return a tuple of (highest_rating_ever, current_rating).

Whenever a rating change occurs, we record it in the diffs array. Return an array with 2 numbers: the highest rating ever achieved and the current rating.

Guaranteed that rating never goes negative.

Example 1:
Input: diffs = [100, -200, 350]
Output: (1750, 1750)
Explanation: Start at 1500. After +100: 1600. After -200: 1400. After +350: 1750. Highest ever = 1750.
"""


def solution(diffs):
    raise NotImplementedError


def test_example():
    sol = solution([100, -200, 350])
    assert_equal(sol, (1750, 1750))


# Run: python3 -m neetcode75.specific.rating_over_time
if __name__ == "__main__":
    run_tests()
