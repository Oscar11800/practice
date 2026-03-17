from typing import List
from test_runner import assert_equal, run_tests
import heapq
'''
1046. Last Stone Weight

You are given an array of integers stones where stones[i] is the weight of the ith stone.

Simulation:
- Each step: choose the two heaviest stones (x and y), smash them together.
- If x == y: both destroyed.
- If x < y: x destroyed, y becomes y - x.
- Continue until at most one stone remains.

Return the weight of the last remaining stone, or 0 if none remain.

Example 1:
  Input: stones = [2,3,6,2,4]
  Output: 1
  Explanation: 6&4→2, [2,3,2,2]; 3&2→1, [1,2,2]; 2&2→destroyed, [1]

Example 2:
  Input: stones = [1,2]
  Output: 1

Constraints:
  1 <= stones.length <= 20
  1 <= stones[i] <= 100
'''


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        Return the weight of the last remaining stone after simulation.

        :param stones: Array of stone weights.
        :return: Last stone weight, or 0 if none remain.
        """
        stones = list(map(lambda s: -s, stones))
        heapq.heapify(stones)
        while len(stones) >= 2:
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)
            diff = s2 - s1
            if diff != 0:
                heapq.heappush(stones, -diff)
        if len(stones):
            return -stones[0]
        else:
            return 0


# ========== TESTS ==========

def test_example1():
    """Example 1: [2,3,6,2,4] -> 1."""
    sol = Solution()
    assert_equal(sol.lastStoneWeight([2, 3, 6, 2, 4]), 1)


def test_example2():
    """Example 2: [1,2] -> 1."""
    sol = Solution()
    assert_equal(sol.lastStoneWeight([1, 2]), 1)


if __name__ == "__main__":
    run_tests()