from typing import List
from neetcode75.test_runner import assert_equal, run_tests
"""
128. Longest Consecutive Sequence

Given an array of integers nums, return the length of the longest consecutive
sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is
exactly 1 greater than the previous element. The elements do not have to be
consecutive in the original array.

You must write an algorithm that runs in O(n) time.

Example 1:
  Input: nums = [2,20,4,10,3,4,5]
  Output: 4
  Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:
  Input: nums = [0,3,2,5,4,6,1,1]
  Output: 7

Constraints:
  0 <= nums.length <= 1000
  -10^9 <= nums[i] <= 10^9
"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Return the length of the longest consecutive sequence in O(n) time.
        - Duplicates should not break sequence counting.
        """
        uniques = set(nums)
        largest = 0

        while len(uniques) > 0:
            seq = 1
            og_curr = uniques.pop()
            curr = og_curr
            while curr - 1 in uniques:
                uniques.remove(curr-1)
                seq += 1
                curr -= 1
            curr = og_curr
            while curr + 1 in uniques:
                uniques.remove(curr+1)
                seq += 1
                curr += 1
            largest = max(largest, seq)
        return largest

            
        


# ========== TESTS ==========

def test_example1():
    """Example 1 from prompt."""
    sol = Solution()
    nums = [2, 20, 4, 10, 3, 4, 5]
    assert_equal(sol.longestConsecutive(nums), 4)


def test_example2():
    """Example 2 from prompt."""
    sol = Solution()
    nums = [0, 3, 2, 5, 4, 6, 1, 1]
    assert_equal(sol.longestConsecutive(nums), 7)


def test_empty():
    """Edge case: empty input."""
    sol = Solution()
    assert_equal(sol.longestConsecutive([]), 0)


def test_single():
    """Edge case: one number."""
    sol = Solution()
    assert_equal(sol.longestConsecutive([42]), 1)


def test_no_consecutive_neighbors():
    """No adjacent integer values."""
    sol = Solution()
    assert_equal(sol.longestConsecutive([10, 30, 50]), 1)


if __name__ == "__main__":
    run_tests()