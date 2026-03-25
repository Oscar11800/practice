from neetcode75.test_runner import assert_equal, run_tests
from typing import List

"""
Coin Change

You are given an integer array coins representing coins of different
denominations and an integer amount representing a target amount of money.

Return the fewest number of coins needed to make up the exact target amount.
If it is impossible to make up the amount, return -1.

You may assume that you have an unlimited number of each coin.

Example 1:
Input: coins = [1,5,10], amount = 12
Output: 3
Explanation: 12 = 10 + 1 + 1.

Example 2:
Input: coins = [2], amount = 3
Output: -1
Explanation: The amount of 3 cannot be made up with coins of 2.

Example 3:
Input: coins = [1], amount = 0
Output: 0
Explanation: Choosing 0 coins is a valid way to make up 0.

Constraints:
1 <= coins.length <= 10
1 <= coins[i] <= 2^31 - 1
0 <= amount <= 10000
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            minimum = float('inf')
            for coin in coins:
                if (i - coin >= 0 and
                    dp[i - coin] != -1 and
                    (dp[i-coin] + 1) < minimum): 
                    minimum = dp[i - coin] + 1
            if minimum == float('inf'):
                dp[i] = -1
            else: 
                dp[i] = minimum
        return dp[amount]



def test_example1():
    sol = Solution()
    assert_equal(sol.coinChange([1,5,10], 12), 3)


def test_example2():
    sol = Solution()
    assert_equal(sol.coinChange([2], 3), -1)


def test_example3():
    sol = Solution()
    assert_equal(sol.coinChange([1], 0), 0)


# Run: python3 -m neetcode75.dp.coin_change
if __name__ == "__main__":
    run_tests()
