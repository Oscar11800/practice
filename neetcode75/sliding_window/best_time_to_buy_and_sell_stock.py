from typing import List
from neetcode75.test_runner import assert_equal, run_tests

"""
Best Time to Buy and Sell Stock
Easy

You are given an integer array prices where prices[i] is the price of NeetCoin
on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in
the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any
transactions, in which case the profit would be 0.

Example 1:
Input: prices = [10,1,5,6,7,1]
Output: 6
Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.

Example 2:
Input: prices = [10,8,7,5,2]
Output: 0
Explanation: No profitable transactions can be made, thus the max profit is 0.

Constraints:
1 <= prices.length <= 100
0 <= prices[i] <= 100
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        raise NotImplementedError


def test_example1():
    sol = Solution()
    assert_equal(sol.maxProfit([10, 1, 5, 6, 7, 1]), 6)


def test_example2():
    sol = Solution()
    assert_equal(sol.maxProfit([10, 8, 7, 5, 2]), 0)


def test_single_day():
    sol = Solution()
    assert_equal(sol.maxProfit([4]), 0)


# Run: python3 -m neetcode75.sliding_window.best_time_to_buy_and_sell_stock
if __name__ == "__main__":
    run_tests()
